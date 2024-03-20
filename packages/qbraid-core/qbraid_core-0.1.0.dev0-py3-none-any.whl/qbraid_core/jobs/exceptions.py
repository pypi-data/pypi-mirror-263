# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module defining custom exceptions for the qBraid jobs module.

"""

from qbraid_core.exceptions import QbraidException


class QbraidJobError(QbraidException):
    """Base class for errors raised by the qBraid jobs module."""
