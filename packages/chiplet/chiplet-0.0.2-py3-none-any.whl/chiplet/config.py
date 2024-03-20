import logging
import os
from typing import Dict, List, Tuple, Union, Optional, Any
from pathlib import Path
from dataclasses import field, asdict

import yaml
from pydantic import ConfigDict, field_validator
from pydantic.dataclasses import dataclass

from chiplet.constants import CHIPLET_MODEL_FILE, CHIPLET_DATA_DIR, CHIPLET_CONTAINER_WORKDIR
from chiplet.render_options import DockerRenderContext

logger = logging.getLogger(__name__)


@dataclass
class _ImageNode:
    """Node in the dependency graph."""

    name: str
    """Name of the node."""

    root: bool = field(default=False)
    """Whether the node is the root node."""

    children: List[str] = field(default_factory=list)
    """List of children for the node."""

    def is_leaf(self) -> bool:
        """Check if the node is a leaf node."""
        return not len(self.children)


@dataclass(config=ConfigDict(extra="forbid"))
class ImageTarget:
    """Chiplet configuration for a docker target specified in `Chipletfile.yaml`
    images:
        <target>:
            image: <repository name>
            base: <base>
            env:
                <key>: <value>
            system:
                - <package>
            conda:
                - <package>
            pip:
                - <package>
            add:
                - <file-mount>
    """

    image: str = field(default=None)
    """Name of the image repository.
    Defaults to <name>:<target> if not specified.
    """

    name: str = field(default="")
    """name of the chiplet project
    """

    target: str = field(default=None)
    """Name of the target."""

    base: str = field(default="debian:buster-slim")
    """Base docker image / target to use (FROM clause in the Dockerfile)."""

    env: Dict[str, str] = field(default_factory=dict)
    """List of environment variables to set."""

    system: Optional[List[str]] = field(default_factory=list)
    """List of system packages to install (via`apt-get`) ."""

    conda: Optional[List[str]] = field(default_factory=list)
    """List of Python packages to install (via `conda/mamba install`)."""

    pip: Optional[List[str]] = field(default_factory=list)
    """List of Python packages to install (via `pip install`)."""

    requirements: Optional[List[str]] = field(default_factory=list)
    """List of Python requirements files to install (via `pip install -r`)."""

    add: Optional[List[str]] = field(default_factory=list)
    """List of files to add into the image (`./entrypoint.sh:/app/entrytpoint.sh`)."""

    workdir: Optional[str] = field(default=None)
    """Working directory for the image (defaults to /app/sb-chiplet ($CHIPLET_PATH) if not set)."""

    run: Optional[List[str]] = field(default_factory=list)
    """List of commands to run in the image under the workdir."""

    entrypoint: Optional[List[str]] = field(default_factory=list)
    """Entrypoint for the image."""

    command: Optional[Union[str, List[str]]] = field(default_factory=list)
    """Command to run in the image."""

    def __post_init__(self):
        if self.target is None:
            self.target = "latest"
        if not self.name:
            raise ValueError("name must be set")

    def __repr__(self):
        return yaml.dump(asdict(self), sort_keys=False)

    def is_base_image(self) -> bool:
        """Check if the base target is root / does not have a parent."""
        return ":" in self.base

    def get_workdir(self) -> str:
        return self.workdir if self.workdir else CHIPLET_CONTAINER_WORKDIR

    def get_add_mounts(self, dk_context: DockerRenderContext) -> List[Tuple[str, str]]:
        workdir = self.get_workdir()
        add_mounts = [
            (CHIPLET_MODEL_FILE, os.path.join(workdir, CHIPLET_MODEL_FILE)),
            (CHIPLET_DATA_DIR, os.path.join(workdir, CHIPLET_DATA_DIR)),
        ]

        if not self.add:
            return add_mounts
        base_path = Path(dk_context.base_path)

        if not base_path.exists():
            raise ValueError(f"Base path {base_path} does not exist")
        for a in self.add:
            from_path, to_path = a.split(":")
            add_mounts.append((from_path, to_path))
        return add_mounts

    @field_validator("command", mode="before")
    def validate_command_version(cls, cmd) -> List[str]:
        """Validate the command."""
        if isinstance(cmd, str):
            cmd = cmd.split(" ")
        elif isinstance(cmd, list):
            pass
        return cmd

    @field_validator("name", mode="before")
    def validate_name(cls, name) -> str:
        """Validate the name."""
        if not name:
            raise ValueError(f"`name` must be a valid string")
        if " " in name:
            raise ValueError(f"`name` cannot have spaces")
        return name

    @field_validator("env", mode="before")
    def validate_env(cls, env) -> Dict[str, str]:
        """Validate the environment variables."""
        if not isinstance(env, dict):
            raise ValueError(f"`env` must be a dictionary (type={type(env)})")
        for key, value in env.items():
            if isinstance(value, int):
                env[key] = str(value)
        return env


@dataclass
class ChipletConfig:
    """Top level Chiplet configuration specified in `Chipletfile.yaml`

    images:
        base-cpu:
            image: my-chiplet-name:latest-base-cpu
            base: python:3.8.10-slim
            env:
                MY_ENV: value

        base-dev:
            ...

        base-prod:
            ...
    """

    images: Dict[str, ImageTarget]
    """Dictionary of targets to build and their configurations."""

    def __post_init__(self):
        """Post-initialization hook."""
        self._target_tree: Dict[str, _ImageNode] = {}
        self._build_target_tree()

    def get_roots(self) -> List[str]:
        """Return all root targets."""
        return [target for target, node in self._target_tree.items() if node.root]

    def root(self) -> str:
        """Return the root target."""
        targets = self.get_roots()
        if len(targets) != 1:
            raise ValueError(f"Expected 1 root target, got {len(targets)}")
        return targets[0]

    def children(self, target: str) -> List[str]:
        """Return the list of children for the given target."""
        return self._target_tree[target].children

    def is_root(self, target: str) -> bool:
        """Check if the given target is a base image."""
        return self._target_tree[target].root

    def is_prod(self) -> bool:
        """Check if the configuration is for production."""
        return self.prod

    def get_template_vars(self, target: str, dk_context: DockerRenderContext) -> Dict[str, Any]:
        image_target = self.images[target]
        image_dict = asdict(image_target)

        image_dict["target"] = target
        image_dict["is_base_image"] = self.is_root(target)
        image_dict["chiplet_env"] = dk_context.env
        image_dict["is_prod"] = dk_context.env == "prod"
        image_dict["add_mounts"] = image_target.get_add_mounts(dk_context)
        image_dict["workdir"] = image_target.get_workdir()

        return image_dict

    @classmethod
    def load_yaml(cls, filename: Union[str, Path]) -> "ChipletConfig":
        """Load the Chiplet configuration from a YAML file.

        Args:
            filename (str): Path to the YAML file.
        Returns:
            ChipletConfig: Chiplet configuration.
        """
        path = Path(filename)
        logger.debug(f"Loading Chiplet configuration from {path}")
        if not path.exists():
            raise ValueError(f"YAML file {path.name} does not exist")
        if not (path.name.endswith(".yaml") or path.name.endswith(".yml")):
            raise ValueError(f"YAML file {path.name} must have a .yaml or .yml extension")

        with path.open("r") as f:
            data = yaml.safe_load(f)
        logger.debug(f"Chiplet configuration: {data}")

        images = data.get("images", {})
        if not images:
            raise ValueError("No images specified in the YAML file")

        for target, config in data["images"].items():
            logger.debug(f"Processing target [{target}]")
            if "name" not in config and config["base"] in data["images"]:
                config["name"] = data["images"][config["base"]].name
            if "target" not in config:
                config["target"] = target

            data["images"][target] = ImageTarget(**config)
        logger.debug(f"Chiplet configuration: {data}")
        return cls(**data)

    def save_yaml(self, filename: str) -> None:
        """Save the Chiplet configuration to a YAML file.

        Args:
            filename (str): Path to the YAML file.
        """
        # Pre-process the config to remove empty lists, etc.
        data = asdict(self)
        for _, config in data["images"].items():
            for key in ["env", "system", "conda", "pip", "requirements", "add", "run", "entrypoint", "command"]:
                if not len(config[key]):
                    del config[key]
            for key in ["workdir"]:
                if config.get(key) is None:
                    del config[key]
        # Save the YAML file
        with open(filename, "w") as f:
            yaml.safe_dump(data, f, sort_keys=False)

    def _build_target_tree(self) -> None:
        """Build the target dependency tree."""
        for idx, (target, config) in enumerate(self.images.items()):
            logger.debug(f"{target} -> {config.base}")

            if idx == 0:
                if not config.is_base_image():
                    raise ValueError(f"First image [{target}] must be a base image")
                self._target_tree[target] = _ImageNode(name=target, root=True)
            else:
                if config.base not in self._target_tree:
                    raise ValueError(
                        f"Base image for derived target `{target}` needs to be one of {list(self._target_tree.keys())}."
                    )
                self._target_tree[target] = _ImageNode(name=target)
                self._target_tree[config.base].children.append(target)
        logger.debug(f"Target dependencies: {self._target_tree}")
