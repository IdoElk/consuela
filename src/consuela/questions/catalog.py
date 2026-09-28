"""Clean-code rubric data: questions, clarifications, and scopes."""

from typesafe_sdk import Noul, Score

QUESTION_CLARIFICATIONS = {
    "does_more_than_one_thing": (
        "Coordinating the observe → choose → execute cycle counts as one responsibility. "
        "Assess whether a function combines responsibilities beyond that cycle, rather than "
        "counting its individual operations as separate responsibilities."
    ),
}

QUESTIONS = {
    "names_hide_intent": Noul(
        instructions=(
            "Do names hide intent: cryptic abbreviations, vague words, or names that mislead about what the "
            "thing is or does?"
        ),
    ),
    "encodings_noise_words": Noul(
        instructions=(
            "Do names carry encodings or noise words: type prefixes, Hungarian notation, member prefixes, or "
            "filler like data, info, manager, object?"
        ),
    ),
    "inconsistent_naming": Noul(
        instructions=(
            "Is one concept named in several ways (fetch/get/retrieve, or the same word used for different things)?"
        ),
    ),
    "does_more_than_one_thing": Noul(
        instructions=(
            "Does any function do more than one thing (you could extract a second function whose name is not "
            "just a restatement of the first)?"
        ),
    ),
    "too_many_arguments": Noul(
        instructions=("Does any function take three or more arguments?"),
    ),
    "flag_or_output_arguments": Noul(
        instructions=(
            "Are boolean flag arguments or output arguments (a function writing its result into an argument) used?"
        ),
    ),
    "hidden_side_effects": Noul(
        instructions=(
            "Does any function have side effects its name does not promise: mutating globals, arguments, or "
            "shared state, doing I/O, or changing something the caller would not expect?"
        ),
    ),
    "mixed_abstraction_levels": Noul(
        instructions=(
            "Does any function mix levels of abstraction, such as high-level business steps next to string "
            "concatenation or byte handling?"
        ),
    ),
    "long_function": Noul(
        instructions=("Is any function longer than about thirty lines?"),
    ),
    "redundant_or_misleading_comments": Noul(
        instructions=("Are there comments that only restate the code, or that are out of date or wrong?"),
    ),
    "commented_out_code": Noul(
        instructions=("Is there commented-out code left in place?"),
    ),
    "noise_comments": Noul(
        instructions=(
            "Are there noise comments: change journals, attributions, closing-brace markers, mandated "
            "boilerplate, or comments that compensate for unclear code?"
        ),
    ),
    "related_code_far_apart": Noul(
        instructions=(
            "Are related things placed far apart: variables declared far from their use, callers far from "
            "callees, no blank lines separating concepts?"
        ),
    ),
    "inconsistent_formatting": Noul(
        instructions=(
            "Is formatting inconsistent within the file: indentation, spacing, line length, or brace style "
            "varying without reason?"
        ),
    ),
    "train_wrecks": Noul(
        instructions=(
            "Are there chains of calls that navigate through several objects (a.getB().getC().doD()), "
            "breaking the Law of Demeter?"
        ),
    ),
    "exposed_internals": Noul(
        instructions=(
            "Are object internals exposed (public fields, getters and setters on everything) or are there "
            "hybrids that are half object, half data structure?"
        ),
    ),
    "returns_null": Noul(
        instructions=("Does the code return null, undefined, -1 or another sentinel to signal failure?"),
    ),
    "error_codes": Noul(
        instructions=("Are error codes or status booleans the caller must check used instead of exceptions?"),
    ),
    "swallowed_errors": Noul(
        instructions=("Is any error caught and ignored, logged and dropped, or handled with an empty catch block?"),
    ),
    "error_handling_tangled": Noul(
        instructions=("Is error handling interleaved with the main logic rather than separated from it?"),
    ),
    "hard_to_test": Noul(
        instructions=(
            "Would this be hard to unit-test as written: hidden dependencies, globals, clocks, randomness, "
            "or I/O tangled with logic?"
        ),
    ),
    "unclear_tests": Noul(
        instructions=(
            "Are the tests unclear: several concepts or assertions per test, no clear build-operate-check "
            "structure, or names that do not say what is tested?"
        ),
    ),
    "class_does_too_much": Noul(
        instructions=(
            "Does a class or module have more than one responsibility or low cohesion (methods that do not "
            "share the instance variables)?"
        ),
    ),
    "rigid_to_change": Noul(
        instructions=(
            "Would a likely change require modifying existing code in several places rather than extending "
            "it (Open-Closed Principle violated)?"
        ),
    ),
    "duplication": Noul(
        instructions=("Is there duplicated logic that should be one function or abstraction?"),
    ),
    "magic_numbers": Noul(
        instructions=("Are there unexplained literal numbers or strings where a named constant belongs?"),
    ),
    "dead_code_or_clutter": Noul(
        instructions=("Is there dead code, unused variables or imports, uncalled functions, or other clutter?"),
    ),
    "obscured_intent": Noul(
        instructions=("Is intent obscured by dense expressions, clever tricks, or missing explanatory variables?"),
    ),
    "switch_over_polymorphism": Noul(
        instructions=("Are if/else or switch chains on a type or flag used where polymorphism would be cleaner?"),
    ),
    "feature_envy": Noul(
        instructions=("Does a method work more with another object's data than its own?"),
    ),
    "leaves_it_worse": Noul(
        instructions=(
            "Judging the change shown in the diff: does it leave the code worse than it found it (the Boy "
            "Scout Rule broken)?"
        ),
    ),
    "function_size": Score(
        instructions=(
            "How large are the functions? Sprawling (screens long), Long (30+ lines), Moderate (10–30), "
            "Short (under 10), Tiny (a handful of lines). Judge the typical function."
        ),
        criteria=["Sprawling", "Long", "Moderate", "Short", "Tiny"],
    ),
    "nesting": Score(
        instructions=(
            "How deep is the control-flow nesting? Arrow-shaped (5+ levels), Deep (4), Moderate (3), Shallow "
            "(2), Flat (1 or guard clauses only)."
        ),
        criteria=["Arrow-shaped", "Deep", "Moderate", "Shallow", "Flat"],
    ),
    "verdict": Score(
        instructions=(
            "What would Uncle Bob say in review? Rewrite it, Refactor (substantial restructuring), Tidy up "
            "(a few extractions and renames), Nitpicks (cosmetic), Ship it."
        ),
        criteria=["Rewrite it", "Refactor", "Tidy up", "Nitpicks", "Ship it"],
    ),
}

QUESTION_SCOPES = {"unclear_tests": "test", "leaves_it_worse": "patch"}
