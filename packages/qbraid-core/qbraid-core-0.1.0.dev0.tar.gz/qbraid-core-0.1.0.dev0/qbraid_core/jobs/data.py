# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module for serving data about qBraid quantum jobs.

"""
from typing import Any, Dict, List, Optional, Tuple

from qbraid_core.session import QbraidSession


def get_jobs(
    query: Optional[Dict[str, Any]] = None,
    session: Optional[QbraidSession] = None,
) -> Tuple[List[List[str]], str]:
    """Queries qBraid API for user quantum jobs."""
    query = query or {}
    session = session or QbraidSession()
    jobs = session.post("/get-user-jobs", json=query).json()
    max_results = query.pop("numResults", 10)
    num_jobs = 0
    job_data = []
    for document in jobs:
        job_id = document.get("qbraidJobId", document.get("_id"))
        if job_id is None:
            continue
        created_at = document.get("createdAt")
        if created_at is None:
            timestamps = document.get("timestamps", {})
            created_at = timestamps.get("createdAt", timestamps.get("jobStarted"))
        status = document.get("qbraidStatus", document.get("status", "UNKNOWN"))
        num_jobs += 1
        job_data.append([job_id, created_at, status])

    if num_jobs == 0:  # Design choice whether to display anything here or not
        if len(query) == 0:
            msg = f"No jobs found for user {session.user_email}"
        else:
            msg = "No jobs found matching given criteria"
    elif num_jobs < max_results:
        msg = f"Displaying {num_jobs}/{num_jobs} jobs matching query"
    elif len(query) > 0:
        plural = "s" if num_jobs > 1 else ""
        msg = f"Displaying {num_jobs} most recent job{plural} matching query"
    else:
        msg = f"Displaying {num_jobs} most recent jobs"
    return job_data, msg
