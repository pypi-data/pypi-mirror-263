"""
This module implements and instantiates the common configuration class used in the project.
"""

# ───────────────────────────────────────────────────── imports ────────────────────────────────────────────────────── #

from pathlib import Path

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                           specifies all modules that shall be loaded and imported into the                           #
#                                current namespace when we use 'from package import *'                                 #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #

__all__ = ["conf_mgr"]


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                                Configuration Manager                                                 #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #


class ConfManager:
    """Configuration Manager class"""

    # paths for dev
    path_root: Path = Path(__file__).parent.parent.parent.resolve()  # takeoff_launcher/
    path_src: Path = path_root / "src"  # takeoff_launcher/src/

    # paths to the scripts
    path_package: Path = Path(__file__).parent.resolve()  # takeoff_launcher/
    path_version: Path = path_package / "version.txt"  # takeoff_launcher/version.txt

    # version
    current_cli_version: str = path_version.read_text().strip()
    current_takeoff_version: str = "0.13.0"

    # takeoff image
    image_name: str = "tytn/takeoff"
    image_tag_gpu: str = current_takeoff_version + "-gpu"  # 0.13.0-gpu
    image_tag_cpu: str = current_takeoff_version + "-cpu"  # 0.13.0-cpu


# ─────────────────────────────────────────────── ConfManager Instance ─────────────────────────────────────────────── #

conf_mgr = ConfManager()
