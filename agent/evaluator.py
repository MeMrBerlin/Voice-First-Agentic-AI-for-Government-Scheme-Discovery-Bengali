# agent/evaluator.py

"""
Agent Evaluator
---------------
Evaluates the result returned by the executor
and decides the next high-level outcome.
"""


def evaluate(execution_result: dict):
    """
    Evaluate executor output and return evaluation status.

    Possible return values:
    - SUCCESS
    - NO_ELIGIBLE_SCHEME
    - ERROR
    - CONTINUE
    """

    if not execution_result or "status" not in execution_result:
        return "ERROR"

    status = execution_result["status"]

    if status == "SUCCESS":
        return "SUCCESS"

    if status == "NO_ELIGIBLE_SCHEME":
        return "NO_ELIGIBLE_SCHEME"

    if status == "SCHEME_NOT_FOUND":
        return "ERROR"

    return "CONTINUE"
