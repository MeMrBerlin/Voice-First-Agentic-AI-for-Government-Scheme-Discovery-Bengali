# agent/planner.py

"""
Agent Planner
-------------
Decides the next action based on conversation memory.
Implements explicit agent planning logic.
"""

def plan(memory):
    """
    Decide the next action for the agent.

    Possible actions:
    - ASK_AGE
    - ASK_INCOME
    - ASK_OCCUPATION
    - ASK_STATE
    - CHECK_ELIGIBILITY
    """

    if memory.get("age") is None:
        return "ASK_AGE"

    if memory.get("income") is None:
        return "ASK_INCOME"

    if memory.get("occupation") is None:
        return "ASK_OCCUPATION"

    if memory.get("state") is None:
        return "ASK_STATE"

    return "CHECK_ELIGIBILITY"
