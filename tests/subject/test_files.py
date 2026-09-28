"""Subject files: target expansion, scope validation, source/patch reading with provenance, and test-path detection."""

import pytest

pytestmark = pytest.mark.skip(reason="scenario placeholder; not implemented")


def test_directory_lists_nested_python_files_sorted():
    """Given pkg with zeta.py, alpha.py and nested/inner.py, when listed, then the result is alpha.py, nested/inner.py,
    zeta.py sorted by path.
    """


def test_directory_listing_skips_non_python_files():
    """Given pkg with notes.txt beside alpha.py, when listed, then only alpha.py is returned."""


def test_directory_listing_skips_hidden_directories_and_files():
    """Given pkg/.hidden/skipped.py and pkg/.secret.py, when listed, then neither appears in the result."""


def test_directory_listing_ignores_hidden_parents_above_the_target():
    """Given a target directory that itself lives under a dot-directory, when listed, then its Python files are still
    returned.
    """


def test_directory_named_like_python_file_is_not_listed():
    """Given pkg/odd.py/ as a directory beside pkg/alpha.py, when the directory is listed, then only alpha.py is
    returned.
    """


def test_directory_without_python_files_is_rejected():
    """Given a directory holding only notes.txt, when listed, then ValueError 'No Python files found under <dir>.' is
    raised.
    """


def test_file_targets_are_kept_as_given():
    """Given file paths first.py and second.py, when expanded, then the tuple (first.py, second.py) is returned
    unchanged.
    """


def test_directory_target_is_replaced_by_its_python_files_in_position():
    """Given pkg then first.py, when expanded, then pkg's sorted Python files come first followed by first.py."""


def test_duplicate_targets_keep_first_position():
    """Given first.py, pkg and first.py again, when expanded, then first.py appears once at its first position."""


def test_expanded_targets_are_a_tuple():
    """Given [first.py, pkg], when expanded, then a tuple is returned, suitable for AuditScope.paths."""


def test_scope_without_paths_is_rejected():
    """Given a scope with no paths, when validated, then ValueError 'Each file-audit request requires exactly one
    target.' is raised.
    """


def test_scope_with_several_paths_is_rejected():
    """Given a scope with one.py and two.py, when validated, then ValueError 'Each file-audit request requires exactly
    one target.' is raised.
    """


def test_scope_with_non_python_file_is_rejected():
    """Given scope one.js, when validated, then ValueError 'Only Python files are supported: one.js' is raised."""


def test_scope_path_without_py_suffix_is_rejected():
    """Given a directory-like scope path pkg with no .py suffix, when validated, then ValueError 'Only Python files are
    supported: pkg' is raised.
    """


def test_scope_validation_does_not_touch_the_filesystem():
    """Given an invalid scope whose paths do not exist, when validated, then the scope error is raised rather than a
    file-not-found error.
    """


def test_source_is_read_as_complete_text():
    """Given target.py containing a two-line function, when read, then the source equals the file text exactly."""


def test_source_is_read_byte_for_byte_with_crlf():
    """Given target.py written with CRLF line endings, when read, then the source encodes back to the identical bytes
    and is not newline-normalized.
    """


def test_provenance_records_posix_path_and_source_sha256():
    """Given target.py, when read, then provenance is {'file': posix path, 'source_sha256': sha256 of the file
    bytes}.
    """


def test_source_sha256_changes_when_only_newlines_change():
    """Given the same file read with CRLF and then with LF endings, then the two source_sha256 values differ."""


def test_missing_patch_reads_as_empty_text():
    """Given a scope whose patch is None, when read, then the patch text is the empty string."""


def test_patch_text_is_read_verbatim():
    """Given change.diff containing '-old\\n+new\\n', when read, then the patch text equals that content."""


def test_non_utf8_patch_fails_to_decode():
    """Given a patch file containing invalid UTF-8 bytes, when read, then a decode error is raised."""


def test_missing_target_fails_to_read():
    """Given a scope pointing at missing.py, when read, then a file-not-found error is raised."""


def test_missing_patch_file_fails_to_read():
    """Given a scope whose patch points at missing.diff, when read, then a file-not-found error is raised."""


def test_non_utf8_source_fails_to_decode():
    """Given a target file containing invalid UTF-8 bytes, when read, then a decode error is raised."""


def test_paths_under_test_directories_are_tests():
    """Given a path under tests/, test/, spec(s)/ or __tests__/, when classified, then it is a test path."""


def test_test_prefixed_python_files_are_tests():
    """Given test_service.py at any depth, when classified, then it is a test path."""


def test_dot_test_and_dot_spec_files_are_tests():
    """Given app.test.ts or app.spec.js, when classified, then it is a test path."""


def test_test_path_detection_is_case_insensitive():
    """Given Tests/Service.py or TEST_service.py, when classified, then it is a test path."""


def test_ordinary_source_paths_are_not_tests():
    """Given src/service.py, src/contest.py or src/testing_utils.py, when classified, then none is a test path."""
