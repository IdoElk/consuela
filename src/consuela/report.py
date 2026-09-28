"""Format one audit report from a Jev response."""

from typesafe_sdk import Noul

from consuela.jev.request import validate_answers
from consuela.questions.catalog import QUESTIONS

MAX_SMELL_PROBABILITY = 0.2
MIN_NO_SMELL_PROBABILITY = 1 - MAX_SMELL_PROBABILITY


def acceptance_report(response, questions):
    validate_answers(response, questions)
    checks = {
        name: {
            "no_smell_probability": 1 - response.answers[name].noul,
            "passed": response.answers[name].noul <= MAX_SMELL_PROBABILITY,
        }
        for name, question in questions.items()
        if isinstance(question, Noul)
    }
    return {
        "minimum_no_smell_probability": MIN_NO_SMELL_PROBABILITY,
        "skipped_by_scope": sorted(QUESTIONS.keys() - questions.keys()),
        "booleans": checks,
        "passed": bool(checks) and all(check["passed"] for check in checks.values()),
    }


def format_report(response, audit):
    return {
        **response.model_dump(),
        **audit.provenance,
        "request_bytes": audit.byte_count,
        "acceptance": acceptance_report(response, audit.questions),
    }
