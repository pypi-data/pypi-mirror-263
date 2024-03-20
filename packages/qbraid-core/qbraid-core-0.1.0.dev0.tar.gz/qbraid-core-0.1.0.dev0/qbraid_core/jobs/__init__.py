# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module serving qBraid jobs information.

.. currentmodule:: qbraid_core.jobs

Functions
----------

.. autosummary::
   :toctree: ../stubs/

   get_jobs
   jobs_supported_enabled

Exceptions
------------

.. autosummary::
   :toctree: ../stubs/

   QbraidJobError

"""
from .data import get_jobs
from .exceptions import QbraidJobError
from .state import jobs_supported_enabled
