"""Select catalog questions by audit scope and wrap their review instructions."""

import pytest

pytestmark = pytest.mark.skip(reason="scenario placeholder; not implemented")


def test_source_file_without_patch_selects_no_scoped_questions():
    """Given src/service.py and an empty patch, neither unclear_tests nor leaves_it_worse is selected."""


def test_test_file_without_patch_selects_unclear_tests():
    """Given tests/test_service.py and an empty patch, unclear_tests is selected and leaves_it_worse is not."""


def test_source_file_with_patch_selects_leaves_it_worse():
    """Given src/service.py and a non-empty patch, leaves_it_worse is selected and unclear_tests is not."""


def test_test_file_with_patch_selects_both_scoped_questions():
    """Given tests/test_service.py and a non-empty patch, both unclear_tests and leaves_it_worse are selected."""


def test_test_scope_follows_the_subject_test_path_rule():
    """Given src/test_service.py and an empty patch, unclear_tests is selected because the subject's test-path rule
    classifies it as a test file even outside tests/."""


def test_unscoped_questions_are_always_selected():
    """Given any path and patch, every catalog question without a scope entry is selected."""


def test_selection_preserves_catalog_order():
    """Given any evidence, the selected names appear in the same order as in the catalog."""


def test_review_instructions_wrap_question_text():
    """Given a question without a clarification, the instructions are exactly {'question': original text}."""


def test_review_instructions_add_clarification_when_defined():
    """Given does_more_than_one_thing, the instructions carry the question text plus the cycle clarification."""


def test_review_instructions_omit_clarification_when_undefined():
    """Given class_does_too_much, the instructions have no clarification key."""


def test_review_instructions_carry_no_source_key():
    """Given any question, the wrapped instructions contain only question and optionally clarification, never source."""
