"""Select catalog questions by audit scope and wrap their review instructions."""

from consuela.questions.catalog import QUESTION_CLARIFICATIONS, QUESTION_SCOPES, QUESTIONS
from consuela.subject.files import is_test_path


def selected_questions(path, patch):
    scopes = {"all", "test" if is_test_path(path) else "all", "patch" if patch else "all"}
    return {name: question for name, question in QUESTIONS.items() if QUESTION_SCOPES.get(name, "all") in scopes}


def review_instructions(name, question):
    instructions = {
        "question": question.instructions,
    }
    if name in QUESTION_CLARIFICATIONS:
        instructions["clarification"] = QUESTION_CLARIFICATIONS[name]
    return instructions
