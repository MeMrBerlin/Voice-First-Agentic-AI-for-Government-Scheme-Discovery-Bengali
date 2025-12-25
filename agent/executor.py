# agent/executor.py

"""
Agent Executor
--------------
Executes actions decided by the planner by invoking tools.
"""

from tools.eligibility import check_eligibility
from tools.scheme_db import get_scheme_details


def execute(action: str, memory):
    """
    Execute the given action using tools.

    Returns a dictionary with execution results.
    """

    if action == "CHECK_ELIGIBILITY":
        scheme_key = check_eligibility(memory.data)

        if scheme_key is None:
            return {
                "status": "NO_ELIGIBLE_SCHEME"
            }

        scheme_details = get_scheme_details(scheme_key)

        if scheme_details is None:
            return {
                "status": "SCHEME_NOT_FOUND"
            }

        return {
            "status": "SUCCESS",
            "scheme": scheme_details
        }

    return {
        "status": "WAITING"
    }
