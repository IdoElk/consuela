"""Scenarios for consuela.run: preparing per-file audits, running a batch, and reviewing one audit."""

import pytest

pytestmark = pytest.mark.skip(reason="scenario placeholder; not implemented")


def test_prepare_audit_validates_scope_before_reading_any_file():
    """Given an invalid scope (no paths, several paths, or a non-.py path), when prepare_audit runs, then it raises
    ValueError before any file is opened.
    """


def test_prepare_audit_builds_state_questions_and_request_for_one_file():
    """Given a scope with one Python file and no patch, when prepare_audit runs, then the PreparedAudit carries the
    file's state, its questions, the serialized request and its byte count.
    """


def test_prepare_audit_provenance_merges_source_identity_mode_and_request_hash():
    """Given a single-file scope, when prepare_audit runs, then provenance holds file as the POSIX path of the target,
    source_sha256 of the file bytes, mode 'file-audit', and request_sha256 of the serialized request; a newline-only
    change to the file (CRLF to LF) changes both source_sha256 and request_sha256.
    """


def test_prepare_audit_byte_count_is_compact_request_size():
    """Given any prepared audit, when inspected, then byte_count equals the UTF-8 length of the compact (non-indented)
    JSON of the request body, the size checked against MAX_REQUEST_BYTES, not the length of the indented serialized
    text.
    """


def test_prepare_audit_includes_patch_text_and_patch_questions():
    """Given a single-file scope with a patch file, when prepare_audit runs, then state patch equals the diff text and
    questions include leaves_it_worse.
    """


def test_prepare_audit_rejects_oversized_request_before_any_call():
    """Given a file whose request exceeds the byte budget, when prepare_audit runs, then it raises ValueError and no
    review is attempted.
    """


def test_prepared_audit_is_immutable():
    """Given a PreparedAudit, when a field is assigned, then a FrozenInstanceError is raised."""


def test_prepare_batch_returns_one_audit_per_expanded_file_in_order():
    """Given a scope with a directory and a file, when prepare_batch runs, then it returns one PreparedAudit per
    expanded .py file in expansion order.
    """


def test_prepare_batch_fails_whole_batch_if_any_file_is_invalid():
    """Given two targets where the second has a syntax error, when prepare_batch runs, then SyntaxError is raised and
    no audits are returned.
    """


def test_prepare_batch_propagates_patch_with_several_targets_error():
    """Given two targets and a patch, when prepare_batch runs, then ValueError '--patch requires exactly one target
    file.' is raised.
    """


def test_audit_batch_reviews_each_audit_in_order():
    """Given two prepared audits and a stubbed review, when audit_batch runs, then review is called once per audit in
    order and both reports appear under audits.
    """


def test_audit_batch_passes_only_when_every_report_passes():
    """Given reports where one acceptance fails, when audit_batch runs, then passed is false; when all pass and there
    are no errors, passed is true.
    """


def test_first_operational_failure_records_scoped_error_and_stops():
    """Given review raising TypeSafeError or ValueError on the first audit, when audit_batch runs, then audits is
    empty, errors has one entry of the audit provenance plus type and message, passed is false, and later audits are
    not reviewed.
    """


def test_later_operational_failure_keeps_completed_audits_and_stops():
    """Given three audits where the second review raises, when audit_batch runs, then the first report is kept, one
    scoped error is recorded, and the third audit is never reviewed.
    """


def test_unexpected_exceptions_escape_audit_batch():
    """Given review raising an exception other than TypeSafeError or ValueError, when audit_batch runs, then the
    exception propagates.
    """


def test_review_calls_jev_once_with_audit_state_and_questions():
    """Given a prepared audit and a stubbed jev system_one, when review runs, then system_one is called exactly once
    with the audit's state and questions.
    """


def test_review_returns_formatted_report_of_jev_response():
    """Given a stubbed jev response, when review runs, then the result equals format_report(response, audit)."""


def test_review_propagates_provider_failure_without_retry():
    """Given system_one raising, when review runs, then the error propagates unchanged after a single call."""
