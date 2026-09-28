"""Scenarios for consuela.report: formatting one audit report from a Jev response."""

import pytest

pytestmark = pytest.mark.skip(reason="scenario placeholder; not implemented")


def test_report_contains_model_usage_and_answers_from_response():
    """Given a response with model 'offline-fixture', usage 12/3 and answers, when format_report runs, then the report
    holds the response's model, usage and answers as dumped dicts.
    """


def test_scores_and_choices_remain_descriptive_in_report():
    """Given answers for a Noul, a Score and a Choice question, when format_report runs, then score and choice values
    appear under answers and only the Noul appears under acceptance booleans.
    """


def test_report_preserves_audit_provenance():
    """Given an audit with mode, source_sha256 and request_sha256 provenance, when format_report runs, then those keys
    and values appear at the top level of the report.
    """


def test_report_includes_request_byte_count():
    """Given an audit with byte_count 123, when format_report runs, then request_bytes is 123."""


def test_report_embeds_acceptance_result_for_audit_questions():
    """Given a response and the audit's questions, when format_report runs, then acceptance equals the acceptance
    report for that response and those questions.
    """


def test_provenance_keys_override_response_keys_of_the_same_name():
    """Given a response dump and provenance sharing a key, when format_report runs, then the provenance value wins."""


def test_invalid_answers_make_formatting_fail():
    """Given a response missing a requested answer, when format_report runs, then ValueError is raised instead of a
    report.
    """
