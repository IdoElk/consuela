"""Prepare and run independent file audits."""

from dataclasses import dataclass

from typesafe_sdk import TypeSafeError

from consuela.jev.client import system_one
from consuela.jev.request import build_request
from consuela.questions import questions_for
from consuela.report import format_report
from consuela.subject import prepare
from consuela.subject.files import read_file, validate_scope
from consuela.subject.state import build_state


@dataclass(frozen=True)
class PreparedAudit:
    state: dict
    questions: dict
    provenance: dict
    serialized: str
    byte_count: int


def prepare_audit(scope):
    validate_scope(scope)
    path = scope.paths[0]
    source, patch, provenance = read_file(scope)
    state = build_state(path, source, patch)
    questions = questions_for(path, source, patch)
    serialized, byte_count, request_sha256 = build_request(state, questions)
    provenance = {
        **provenance,
        "mode": "file-audit",
        "request_sha256": request_sha256,
    }
    return PreparedAudit(state, questions, provenance, serialized, byte_count)


def prepare_batch(scope):
    return [prepare_audit(item) for item in prepare(scope)]


def audit_batch(audits):
    reports = []
    errors = []
    for audit in audits:
        try:
            reports.append(review(audit))
        except (TypeSafeError, ValueError) as error:
            errors.append({**audit.provenance, "type": type(error).__name__, "message": str(error)})
            break
    return {
        "audits": reports,
        "errors": errors,
        "passed": not errors and all(report["acceptance"]["passed"] for report in reports),
    }


def review(audit):
    response = system_one(audit.state, audit.questions)
    return format_report(response, audit)
