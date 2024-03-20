# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module for serving quantum jobs information.

"""

import logging
from pathlib import Path
from typing import Optional, Tuple

from qbraid_core.system import get_active_site_packages_path, get_venv_site_packages_path

from .exceptions import QbraidException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _check_proxy(
    proxy_spec: Tuple[str, ...], slug_path: Optional[Path] = None
) -> Tuple[bool, bool]:
    """
    Checks if the specified proxy file exists and contains the string 'qbraid'.

    Args:
        proxy_spec (Tuple[str, ...]): A tuple specifying the path components from 'site-packages'
                                      to the target proxy file, e.g. ("botocore", "httpsession.py").
        slug_path (optional, Path): The base path to prepend to the 'pyenv' directory.

    Returns:
        A tuple of two booleans: The first indicates whether the specified proxy file exists;
        the second, if the file exists, is True if it contains 'qbraid', False otherwise.
    """
    try:
        if slug_path is None:
            site_packages: str = get_active_site_packages_path()
            site_packages_path = Path(site_packages)
        else:
            site_packages_path = get_venv_site_packages_path(slug_path / "pyenv")
    except QbraidException as err:
        logger.debug(err)
        return False, False

    target_file_path = site_packages_path.joinpath(*proxy_spec)

    if not target_file_path.exists():
        return False, False

    try:
        with target_file_path.open("r", encoding="utf-8") as file:
            for line in file:
                if "qbraid" in line:
                    return True, True
        return True, False
    except Exception as err:  # pylint: disable=broad-exception-caught
        logger.debug("Unexpected error checking qBraid proxy: %s", err)

    return True, False


def jobs_supported_enabled(device_lib: str) -> Tuple[bool, bool]:
    """Checks if qBraid Quantum Jobs are supported and if so, checks whether they are enabled.

    Args:
        device_lib (str): The name of the quantum device library, e.g., "braket".

    Returns:
        A tuple of two booleans: The first indicates whether the specified proxy file exists;
        the second, if the file exists, is True if it contains 'qbraid', False otherwise.
    """
    if device_lib == "braket":
        proxy_spec = ("botocore", "httpsession.py")
    else:
        return False, False

    return _check_proxy(proxy_spec)
