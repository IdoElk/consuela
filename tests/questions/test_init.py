"""questions_for: compose derived and scope-selected questions with wrapped instructions."""

import pytest

pytestmark = pytest.mark.skip(reason="scenario placeholder; not implemented")


def test_result_combines_derived_and_selected_questions():
    """Given src/service.py with one function and no patch, the result holds responsibility_coherence, fix_functions
    and every unscoped catalog question."""


def test_ordinary_file_has_twenty_nine_boolean_checks():
    """Given src/service.py, empty source and no patch, exactly twenty-nine Noul questions are returned."""


def test_scoped_questions_require_their_evidence():
    """Given the four path/patch combinations of source vs test file and empty vs non-empty patch, the scoped
    questions returned are none, unclear_tests, leaves_it_worse, and both respectively."""


def test_derived_questions_come_before_catalog_questions():
    """Given source with functions, responsibility_coherence and fix_functions precede the catalog questions in the
    result order."""


def test_every_question_carries_wrapped_instructions():
    """Given any evidence, every returned question's instructions is a dict with the original text under question,
    including derived ones."""


def test_derived_questions_share_identical_wrapped_instructions():
    """Given source with functions, fix_functions and responsibility_coherence have identical wrapped instructions."""


def test_wrapping_preserves_original_question_text():
    """Given tests/test_service.py with a patch, each catalog question's instructions['question'] equals its catalog
    text."""


def test_cycle_clarification_applies_to_function_responsibility():
    """Given src/service.py, does_more_than_one_thing carries the cycle clarification and class_does_too_much carries
    none."""


def test_preparation_does_not_mutate_shared_rubric():
    """Given tests/test_service.py, source 'def run(): pass' and a patch, the catalog model_dump is unchanged after
    the call."""


def test_repeated_calls_return_equal_results():
    """Given the same path, source and patch twice, both results are equal and independent objects."""
