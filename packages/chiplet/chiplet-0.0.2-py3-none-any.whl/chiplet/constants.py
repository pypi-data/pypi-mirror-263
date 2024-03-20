import os
from pathlib import Path

CHIPLET_BASE_DIR = Path(__file__).parent

CHIPLET_CHIPLETFILE_NAME = "Chipletfile.yaml"

CHIPLET_TEMPLATE_DIR = CHIPLET_BASE_DIR / "templates"
CHIPLET_DOCKERFILE_TEMPLATE = "Dockerfile.j2"

TEMPLATE_FILE = lambda x: f"Chipletfile.{x}.j2"

CHIPLET_MODEL_TEMPLATE = "Model.j2"
CHIPLET_MODEL_FILE = "Model.py"
CHIPLET_DATA_DIR = "data"
CHIPLET_CONTAINER_WORKDIR = "/app/sb-chiplet"

CHIPLET_ENV = os.getenv("CHIPLET_ENV", "prod")

CHIPLET_RAY_VERSION = "2.9.3"
CHIPLET_PY_SUFFIX = "py310"
CHIPLET_RAY_TAG = f"{CHIPLET_RAY_VERSION}-{CHIPLET_PY_SUFFIX}"
