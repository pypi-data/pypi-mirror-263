# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module serving qBraid devices information.

.. currentmodule:: qbraid_core.devices

Functions
----------

.. autosummary::
   :toctree: ../stubs/

   get_devices

Exceptions
------------

.. autosummary::
   :toctree: ../stubs/

   QbraidDeviceError

"""
from .data import get_devices
from .exceptions import QbraidDeviceError
