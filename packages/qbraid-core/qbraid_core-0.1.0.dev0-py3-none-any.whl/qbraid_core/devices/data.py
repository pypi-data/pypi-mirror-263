# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module for serving data about qBraid devices.

"""
import datetime
from typing import Any, Dict, List, Optional, Tuple

from qbraid_core.session import QbraidSession


def _get_device_data_msg(num_devices: int, lag: int) -> str:
    """Helper function to return a status message based on the
    number of devices and the lag time."""
    if num_devices == 0:
        return "No results matching given criteria"
    hours, minutes = divmod(lag, 60)
    min_10, _ = divmod(minutes, 10)
    min_display = min_10 * 10
    if hours > 0:
        if minutes > 30:
            return f"Device status updated {hours}.5 hours ago"
        hour_s = "hour" if hours == 1 else "hours"
        return f"Device status updated {hours} {hour_s} ago"
    if minutes < 10:
        min_display = minutes
    return f"Device status updated {min_display} minutes ago"


def get_devices(
    query: Optional[Dict[str, Any]] = None, session: Optional[QbraidSession] = None
) -> Tuple[List[List[str]], str]:
    """Queries qBraid API for all supported quantum devices and returns a list of devices
    that match the query filters. Each device is represented by its own length-4 list
    containing the [provider, name, qbraid_id, status].
    """
    query = query or {}
    session = session or QbraidSession()

    # forward compatibility for casing transition
    if query.get("type") == "SIMULATOR":
        query["type"] = "Simulator"

    # get-devices must be a POST request with kwarg `json` (not `data`) to
    # encode the query. This is because certain queries contain regular
    # expressions which cannot be encoded in GET request `params`.
    devices = session.post("/public/lab/get-devices", json=query).json()

    device_data = []
    tot_dev = 0
    min_lag = 1e7
    for document in devices:
        qbraid_id = document["qbraid_id"]
        name = document["name"]
        provider = document["provider"]
        status_refresh = document["statusRefresh"]
        # timestamp = datetime.datetime.now(datetime.UTC)
        timestamp = datetime.datetime.utcnow()
        if status_refresh is not None:
            format_datetime = str(status_refresh)[:10].split("-") + str(status_refresh)[
                11:19
            ].split(":")
            format_datetime_int = [int(x) for x in format_datetime]
            mk_datime = datetime.datetime(*format_datetime_int)
            lag = (timestamp - mk_datime).seconds
            min_lag = min(lag, min_lag)
        status = document["status"]
        tot_dev += 1
        device_data.append([provider, name, qbraid_id, status])

    device_data.sort()
    lag, _ = divmod(min_lag, 60)

    return device_data, _get_device_data_msg(tot_dev, lag)
