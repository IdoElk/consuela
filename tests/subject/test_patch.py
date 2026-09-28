"""PLANNED: subject patch: split one diff into per-file patches."""

import pytest

pytestmark = pytest.mark.skip(reason="scenario placeholder; not implemented")


def test_single_file_diff_yields_one_patch_for_that_file():
    """PLANNED: Given a diff touching only a.py, when split, then one patch keyed by a.py is returned with the full
    hunk text.
    """


def test_multi_file_diff_yields_one_patch_per_file():
    """PLANNED: Given a diff touching a.py and b.py, when split, then two patches are returned, each containing only
    its own hunks.
    """


def test_split_preserves_hunk_text_byte_for_byte():
    """PLANNED: Given a diff with CRLF lines and trailing whitespace, when split, then each per-file patch preserves
    the text as read.
    """


def test_audited_file_absent_from_diff_gets_empty_patch():
    """PLANNED: Given a diff touching only a.py and an audit of c.py, when patches are matched, then c.py receives an
    empty patch.
    """


def test_renamed_file_patch_is_keyed_by_new_path():
    """PLANNED: Given a diff renaming old.py to new.py, when split, then the patch is keyed by new.py."""


def test_deleted_file_patch_is_not_matched_to_an_audit_target():
    """PLANNED: Given a diff deleting gone.py, when split, then no audited file receives gone.py's patch."""


def test_diff_path_prefixes_are_stripped_for_matching():
    """PLANNED: Given a git diff with a/ and b/ prefixes, when split, then patches are keyed by the repository-relative
    path without prefix.
    """


def test_non_diff_input_is_rejected():
    """PLANNED: Given text that contains no file headers, when split, then a ValueError naming the patch file is
    raised.
    """
