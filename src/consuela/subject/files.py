"""Resolve audit targets to Python files and read their source and patch text."""

import hashlib
import re


def python_files_under(directory):
    files = sorted(
        path
        for path in directory.rglob("*.py")
        if path.is_file() and not any(part.startswith(".") for part in path.relative_to(directory).parts)
    )
    if not files:
        raise ValueError(f"No Python files found under {directory}.")
    return files


def expand_targets(paths):
    targets = []
    for path in paths:
        targets.extend(python_files_under(path) if path.is_dir() else [path])
    return tuple(dict.fromkeys(targets))


def validate_scope(scope):
    if len(scope.paths) != 1:
        raise ValueError("Each file-audit request requires exactly one target.")
    path = scope.paths[0]
    if path.suffix != ".py":
        raise ValueError(f"Only Python files are supported: {path}")


def read_file(scope):
    path = scope.paths[0]
    source = path.read_bytes().decode("utf-8")
    patch = scope.patch.read_text(encoding="utf-8") if scope.patch else ""
    provenance = {
        "file": path.as_posix(),
        "source_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
    }
    return source, patch, provenance


def is_test_path(path):
    return (
        re.search(
            r"(^|/)(__tests__|tests?|specs?)/|\.(test|spec)\.[a-z]+$|(^|/)test_[^/]+\.py$",
            path.as_posix(),
            re.IGNORECASE,
        )
        is not None
    )
