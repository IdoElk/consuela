"""Run independent audits of Python files."""

import json
from pathlib import Path

import click
from dotenv import load_dotenv

from consuela.run import audit_batch, prepare_batch
from consuela.subject import AuditScope

EXISTING_FILE = click.Path(exists=True, dir_okay=False, path_type=Path)
EXISTING_PATH = click.Path(exists=True, path_type=Path)
OUTPUT_FILE = click.Path(dir_okay=False, path_type=Path)


def write_requests(audits, destination):
    requests = {"requests": [json.loads(audit.serialized) for audit in audits]}
    serialized = json.dumps(requests, indent=2)
    if destination:
        with destination.open("x", encoding="utf-8") as output:
            output.write(serialized + "\n")
    return serialized


@click.command()
@click.argument("paths", nargs=-1, required=True, type=EXISTING_PATH)
@click.option("--patch", type=EXISTING_FILE, help="Diff for a single file-audit, enabling the patch-only question.")
@click.option("--dry-run", is_flag=True, help="Print requests without calling TypeSafe.")
@click.option("--dump-request", type=OUTPUT_FILE, help="Save the request batch before any API calls.")
@click.option("--env-file", type=EXISTING_FILE, help="Load secrets here; default: .env in the working directory.")
@click.version_option()
def main(paths, patch, dry_run, dump_request, env_file):
    """Audit Python PATHS with Jev. Directories expand to every .py file inside; each file gets an independent audit."""
    try:
        audits = prepare_batch(AuditScope(paths, patch))
        preview = write_requests(audits, dump_request)
        if dry_run:
            click.echo(preview)
            return
        load_dotenv(env_file or Path.cwd() / ".env", override=False)
        report = audit_batch(audits)
    except (OSError, ValueError, SyntaxError) as error:
        raise click.ClickException(str(error)) from error
    click.echo(json.dumps(report, indent=2))
    raise SystemExit(0 if report["passed"] else 1)
