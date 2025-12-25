# tools/eligibility.py

"""
Eligibility Engine Tool
-----------------------
Determines which government scheme a user is eligible for
based on collected profile information.

This is designed as a TOOL that can later be replaced by
an ML model without changing the agent.
"""


def check_eligibility(profile: dict):
    """
    Determine eligible scheme based on user profile.

    Expected profile keys:
    - age (str, digits)
    - income (str, digits)
    - occupation (str)
    - state (str)

    Returns:
    - scheme_key (str) or None
    """

    try:
        age = int(profile.get("age", 0))
        income = int(profile.get("income", 0))
        occupation = profile.get("occupation", "").lower()
    except ValueError:
        # Invalid numeric input
        return None

    # Rule-based eligibility logic (tool-level)
    if age >= 60:
        return "OLD_AGE_PENSION"

    if occupation == "farmer" and income <= 600000:
        return "PM_KISAN"

    return None
