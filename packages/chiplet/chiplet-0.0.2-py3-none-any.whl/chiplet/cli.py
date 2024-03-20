import re
import shutil
from pathlib import Path

import typer
from rich import print
from jinja2 import Environment, FileSystemLoader
from rich.tree import Tree

from chiplet.builder import Chiplet, ChipletConfig
from chiplet.constants import (
    TEMPLATE_FILE,
    CHIPLET_RAY_TAG,
    CHIPLET_MODEL_FILE,
    CHIPLET_TEMPLATE_DIR,
    CHIPLET_MODEL_TEMPLATE,
    CHIPLET_CHIPLETFILE_NAME,
    CHIPLET_DATA_DIR,
)
from chiplet.render_options import DockerRenderContext

app = typer.Typer(invoke_without_command=True)


@app.callback()
def main(ctx: typer.Context):
    """Chiplet generator for Substrate"""
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())


@app.command()
def new(
    name: str = typer.Argument(None, help="Name of the new chiplet. [required]"),
    compute: str = typer.Option("gpu", "--compute", help="Compute env: [cpu, gpu, cu12, inf2, tpuv5, etc]"),
    replace: bool = typer.Option(False, "-f", help="Force: replace chiplet dir if exists", show_default=False),
):
    """Create a chiplet directory with a [Chipletfile, Model.py, data/]"""
    if name is None:
        raise typer.BadParameter("Name of the new chiplet is required.")
    if re.search(r"\s", name):
        raise typer.BadParameter(f"Name {name} is not a valid identifier.")

    path = Path(name)

    if path.exists():
        if replace:
            shutil.rmtree(path)
        else:
            raise typer.BadParameter(f"Directory {name} already exists.")

    path.mkdir(parents=True, exist_ok=True)

    template = Environment(loader=FileSystemLoader(searchpath=CHIPLET_TEMPLATE_DIR))
    chiplet_args = dict(chiplet_name=name, ray_tag=f"{CHIPLET_RAY_TAG}-{compute}")
    templatefile = TEMPLATE_FILE(compute)
    template_path = CHIPLET_TEMPLATE_DIR / templatefile

    if not template_path.exists():
        raise typer.BadParameter(
            f"Support for compute target {compute} not implemented. Create {templatefile} in {CHIPLET_TEMPLATE_DIR} to support this target."
        )

    # TODO(rob) - should we add support for specifying e.g. 2 H100s? Ideally done via the serve yaml, not in Model.py

    chipletfile = template.get_template(templatefile).render(**chiplet_args)
    chipletfile_path = path / CHIPLET_CHIPLETFILE_NAME
    model_path = path / CHIPLET_MODEL_FILE

    with open(chipletfile_path, "w") as f:
        f.write(chipletfile)

    # ChipletConfig.load_yaml(chipletfile_path).save_yaml(chipletfile_path)

    print("\n")
    print("-" * 48)
    print(f"🐣 Created Chipletfile")
    print("-" * 48)
    print("\n")

    with open(chipletfile_path, "r") as f:
        print(f.read())

    model_args = dict(
        use_fastapi=False,
        model_name=name,
    )
    py_model = template.get_template(CHIPLET_MODEL_TEMPLATE).render(**model_args)
    with open(model_path, "w") as f:
        f.write(py_model)

    # add a data directory
    data_dir = path / CHIPLET_DATA_DIR
    data_dir.mkdir(parents=True, exist_ok=True)

    print("\n")
    print("-" * 48)
    print(f"🐥 Configure system with: [bold white]{chipletfile_path}[/bold white]")
    cmd = f"[dim][green]chiplet[/green] render {path}[/dim]"
    print(f"🧙🏼‍♀️ Implement your model at [bold white]{model_path}[/bold white]")
    print(f"🧧 Generate Dockerfile: {cmd}")
    print("-" * 48)
    print("\n")


@app.command()
def render(
    chiplet_dir: str = typer.Argument(None, help="Path to the chiplet directory."),
    filename: str = typer.Option(
        None,
        "--output-filename",
        "-o",
        help="Output filename for the generated Dockerfile.",
    ),
    prod: bool = typer.Option(False, "--prod", help="Generate a production Dockerfile.", show_default=False),
    lint: bool = typer.Option(False, "--lint", help="Lint the generated Dockerfile.", show_default=False),
    build: bool = typer.Option(False, "--build", help="Build the Docker image after generating the Dockerfile."),
    push: bool = typer.Option(False, "--push", help="Push image via docker push", show_default=False),
):
    """Generate the Dockerfile with optional overrides.

    Usage: \n
        chiplet render my-chiplet/ \n
        chiplet render my-chiplet/ -o artifacts/Dockerfile \n
        chiplet render my-chiplet/ --base debian:buster-slim \n
        chiplet render my-chiplet/ --prod --lint \n
        chiplet render my-chiplet/ --build \n
    """
    chiplet_path = Path(chiplet_dir)
    if not chiplet_path.exists():
        raise typer.BadParameter(f"Chiplet directory {chiplet_dir} does not exist.")

    config = ChipletConfig.load_yaml(chiplet_path / CHIPLET_CHIPLETFILE_NAME)

    root = config.root()

    trees = []
    builder = Chiplet(config)
    env = "prod" if prod else "dev"
    if filename is None:
        filename = str(chiplet_path / f"{env}.Dockerfile")

    print("\n")
    print("-" * 48)
    print(f"🐳 Generated Dockerfile for chiplet [bold white]{chiplet_path}[/bold white]")
    print("-" * 48)

    docker_context = DockerRenderContext(base_path=chiplet_path, filename=Path(filename), env=env)
    dockerfiles = builder.render(dk_context=docker_context)

    for target, filename in dockerfiles.items():
        image_target = config.images[target]
        tag = image_target.image or f"{image_target.name}:{target}"

        cmd = f"[dim][green]docker[/green] build -f {filename} --target {target} -t {tag} {chiplet_path}[/dim]"

        tree = Tree(f"Target: [bold white]{target}[/bold white]")
        tree.add(f"[bold green]✓[/bold green] Generated Dockerfile at [bold white]{filename}[/bold white]").add(
            f"Build cmd: {cmd}"
        )

        if lint:
            print("\n")
            print("-" * 48)
            print(f"🕵🏽  Linting Dockerfile for target [bold white]{target}[/bold white]")
            print("-" * 48)
            print("\n")
            builder.lint(filename=filename)

        if build:
            print("\n")
            print("-" * 48)
            print(f"🛳️  Building Docker image for target [bold white]{target}[/bold white]")
            print("-" * 48)
            print("\n")
            builder.build(dk_context=docker_context, target=target, tags=[tag])
            tree.add(
                f"[bold green]✓[/bold green] Built image: target=[bold white]{target}[/bold white], image=[bold white]{tag}[/bold white]"
            )
            if push:
                tree.add(f"[bold red]ⅹ[/bold red] Push not supported yet ([bold white]{tag}[/bold white])")
            trees.append(tree)

        print("\n")
        print(tree)

    if build:
        print("\n")
        print("-" * 48)
        print(f"🌀  Build summary for [bold white]{chiplet_path}[/bold white]")
        print("-" * 48)

    for tree in trees:
        print("\n")
        print(tree)
    print("\n")


@app.command()
def build(
    chiplet_dir: str = typer.Argument(None, help="Path to the chiplet directory."),
    filename: str = typer.Option(
        None,
        "--output-filename",
        "-o",
        help="Output filename for the generated Dockerfile.",
    ),
    prod: bool = typer.Option(False, "--prod", help="Generate a production Dockerfile.", show_default=False),
    push: bool = typer.Option(False, "--push", help="Push image via docker push", show_default=False),
):
    render(
        chiplet_dir=chiplet_dir,
        filename=filename,
        prod=prod,
        lint=False,
        build=True,
        push=push,
    )


@app.command()
def dev(
    chiplet_dir: str = typer.Argument(None, help="Path to the chiplet directory."),
):
    ...


if __name__ == "__main__":
    app()
