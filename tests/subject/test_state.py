"""Subject state: the Jev state dict for one audited file."""

import pytest

pytestmark = pytest.mark.skip(reason="scenario placeholder; not implemented")


def test_state_has_exactly_path_file_patch_and_audit_scope_keys():
    """Given a path, source and patch, when the state is built, then its keys are exactly path, file, patch and
    audit_scope.
    """


def test_state_path_is_posix_string():
    """Given a Path pkg/alpha.py, when the state is built, then state['path'] is the string 'pkg/alpha.py'."""


def test_state_file_is_the_complete_source_unchanged():
    """Given source text with CRLF endings, when the state is built, then state['file'] equals that source exactly."""


def test_state_patch_is_empty_string_without_patch():
    """Given an empty patch text, when the state is built, then state['patch'] is ''."""


def test_state_patch_carries_patch_text_verbatim():
    """Given patch text '-old\\n+new\\n', when the state is built, then state['patch'] equals it."""


def test_state_audit_scope_instructs_file_only_review():
    """Given any inputs, when the state is built, then state['audit_scope'] is 'Review only file. Use patch for diff
    questions.'.
    """


def test_state_order_is_stable_for_serialization():
    """Given any inputs, when the state is built, then keys appear in the order path, file, patch, audit_scope so
    request bytes stay identical.
    """
