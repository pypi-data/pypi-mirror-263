# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module defining custom exceptions for the qBraid environments module.

"""

from qbraid_core.exceptions import QbraidException


class QbraidEnvironmentError(QbraidException):
    """Base class for errors raised by the qBraid environments module."""
