"""Audit subject scope: the scope value and splitting targets into per-file scopes."""

import pytest

pytestmark = pytest.mark.skip(reason="scenario placeholder; not implemented")


def test_scope_defaults_to_no_patch():
    """Given paths (first.py,), when an AuditScope is built without a patch, then its patch is None."""


def test_scope_is_immutable():
    """Given an AuditScope, when a caller assigns to paths or patch, then the assignment is rejected."""


def test_each_file_target_becomes_its_own_scope():
    """Given a scope with first.py and second.py, when prepared, then two scopes are returned in order, each holding
    exactly one path.
    """


def test_directory_targets_expand_in_place():
    """Given a scope with directory pkg then first.py, when prepared, then the per-file scopes are pkg/alpha.py,
    pkg/nested/inner.py, pkg/zeta.py, first.py in that order.
    """


def test_duplicate_targets_keep_first_occurrence():
    """Given a scope listing pkg and pkg/alpha.py again, when prepared, then pkg/alpha.py appears once at its first
    position.
    """


def test_patch_carries_to_the_single_file_scope():
    """Given one file target and a patch path, when prepared, then the single returned scope keeps that patch path."""


def test_patch_with_several_file_targets_is_rejected():
    """Given first.py and second.py with a patch, when prepared, then ValueError '--patch requires exactly one target
    file.' is raised.
    """


def test_patch_with_directory_expanding_to_several_files_is_rejected():
    """Given directory pkg containing a.py and b.py with a patch, when prepared, then ValueError '--patch requires
    exactly one target file.' is raised.
    """


def test_patch_with_directory_expanding_to_one_file_is_accepted():
    """Given a directory containing exactly one Python file and a patch, when prepared, then one scope with that file
    and the patch is returned.
    """


def test_directory_without_python_files_fails_splitting():
    """Given a directory holding only notes.txt, when prepared, then ValueError 'No Python files found under <dir>.' is
    raised before any scope is returned.
    """


def test_splitting_does_not_read_file_contents():
    """Given a target path that does not exist, when prepared, then its scope is returned unchanged and reading
    failures surface only later.
    """
