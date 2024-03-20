from typing import Union
from pathlib import Path
from dataclasses import field, dataclass

from chiplet.constants import CHIPLET_ENV


@dataclass
class DockerRenderContext:
    base_path: Union[str, Path] = field(default=Path.cwd())
    """Docker context dir. Defaults to the current working directory."""

    filename: Union[str, Path] = field(default="Dockerfile")

    env: str = field(default=CHIPLET_ENV)
    """Chiplet environment to use for the build. Generally dev|prod, but can be any custom env too"""
