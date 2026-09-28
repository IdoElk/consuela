"""PLANNED: subject project: package tree and project purpose for state."""

import pytest

pytestmark = pytest.mark.skip(reason="scenario placeholder; not implemented")


def test_package_tree_lists_python_modules_of_the_audited_project():
    """PLANNED: Given a project with src/pkg/a.py and src/pkg/sub/b.py, when the tree is built, then it lists both
    modules in sorted order.
    """


def test_package_tree_excludes_hidden_and_non_python_entries():
    """PLANNED: Given a project with .venv/ and notes.txt, when the tree is built, then neither appears."""


def test_project_purpose_is_read_from_project_metadata():
    """PLANNED: Given a pyproject description, when the purpose is gathered, then it is the description text."""


def test_missing_project_purpose_yields_empty_value_not_error():
    """PLANNED: Given a project without any purpose source, when the purpose is gathered, then an empty value is
    returned rather than an exception.
    """


def test_project_context_is_identical_for_every_file_in_one_batch():
    """PLANNED: Given two files from the same project, when their project context is built, then both receive
    byte-identical tree and purpose.
    """


def test_project_context_does_not_include_other_files_source():
    """PLANNED: Given a project with several modules, when the tree is built, then it holds names only and no source
    text of other files.
    """
