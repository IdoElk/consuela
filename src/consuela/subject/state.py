"""Build the Jev state for one audited file."""


def build_state(path, source, patch):
    return {
        "path": path.as_posix(),
        "file": source,
        "patch": patch,
        "audit_scope": "Review only file. Use patch for diff questions.",
    }
