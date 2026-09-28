"""Questions derived from the file itself: responsibility coherence and the functions to fix."""

import ast

from typesafe_sdk import Choice, Score


def derived_questions(file_content):
    all_functions = [
        node.name
        for node in ast.walk(ast.parse(file_content))
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]

    instruction = (
        "does this file own a coherent responsibility, or does it combine concerns that change for independent reasons?"
    )
    questions = {
        "responsibility_coherence": Score(
            instructions=instruction,
            criteria=[
                "One coherent responsibility; the parts support the same purpose.",
                "Multiple distinct responsibilities with independent reasons to change.",
                "Multiple independent responsibilities tightly interwoven throughout the file.",
            ],
        ),
    }
    if all_functions:
        questions["fix_functions"] = Choice(instructions=instruction, criteria={f: None for f in all_functions})
    return questions
