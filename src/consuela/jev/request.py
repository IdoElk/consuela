"""Build, size-check, and serialize the Jev request body; validate the answers it returns."""

import hashlib
import json

from typesafe_sdk import Noul

# Jev limits, verified against the live service on 2026-09-26: 64k tokens per
# request (state plus every question) and 32k tokens for state plus the longest
# question. Python source measured 4.5-4.8 bytes per token; these guards assume
# 4 bytes per token and round down, leaving roughly a 10-20% margin.
MAX_REQUEST_BYTES = 240_000
MAX_QUESTION_BYTES = 120_000


def build_request(state, questions):
    request = {"state": state, "questions": {name: question.model_dump() for name, question in questions.items()}}
    byte_count = validate_request_size(request)
    serialized = json.dumps(request, indent=2)
    request_sha256 = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
    return serialized, byte_count, request_sha256


def validate_request_size(request):
    byte_count = len(json.dumps(request).encode("utf-8"))
    if byte_count > MAX_REQUEST_BYTES:
        raise ValueError(
            f"Review payload is {byte_count} bytes; limit is {MAX_REQUEST_BYTES}. "
            "Reduce the supplied file or patch size."
        )
    for name, question in request["questions"].items():
        individual = {"state": request["state"], "questions": {name: question}}
        individual_bytes = len(json.dumps(individual).encode("utf-8"))
        if individual_bytes > MAX_QUESTION_BYTES:
            raise ValueError(
                f"State plus question {name!r} is {individual_bytes} bytes; "
                f"limit is {MAX_QUESTION_BYTES}. Reduce the supplied file or patch size."
            )
    return byte_count


def validate_answers(response, questions):
    missing = questions.keys() - response.answers.keys()
    if missing:
        raise ValueError(f"Review response omitted questions: {', '.join(sorted(missing))}")
    for name, question in questions.items():
        answer = response.answers[name]
        if answer.type != question.type:
            raise ValueError(f"Review answer {name!r} has type {answer.type!r}; expected {question.type!r}.")
        if isinstance(question, Noul) and not 0 <= answer.noul <= 1:
            raise ValueError(f"Review answer {name!r} has an invalid smell probability: {answer.noul!r}.")
