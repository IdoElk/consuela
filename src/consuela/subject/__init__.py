"""Audit subject: the scope of files and patch to audit."""

from dataclasses import dataclass, replace
from pathlib import Path

from consuela.subject.files import expand_targets


@dataclass(frozen=True)
class AuditScope:
    paths: tuple[Path, ...]
    patch: Path | None = None


def prepare(scope):
    scope = replace(scope, paths=expand_targets(scope.paths))
    if scope.patch and len(scope.paths) != 1:
        raise ValueError("--patch requires exactly one target file.")
    return [replace(scope, paths=(path,)) for path in scope.paths]
