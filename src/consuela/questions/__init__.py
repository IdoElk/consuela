"""Clean-code rubric and question selection for each audit scope."""

from consuela.questions.derived import derived_questions
from consuela.questions.selection import review_instructions, selected_questions


def questions_for(path, file_content, patch):
    questions = derived_questions(file_content)
    questions.update(selected_questions(path, patch))
    return {
        name: question.model_copy(update={"instructions": review_instructions(name, question)})
        for name, question in questions.items()
    }
