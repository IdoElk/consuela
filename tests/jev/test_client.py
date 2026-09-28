"""Single Jev system_one call through the TypeSafe client."""

import pytest

pytestmark = pytest.mark.skip(reason="scenario placeholder; not implemented")


def test_one_call_sends_state_and_questions_unchanged():
    """Given a state dict and questions {"smell": Noul()} with the TypeSafe client stubbed, when system_one is called,
    then the client's system_one is called exactly once with state=<that state> and questions=<those questions>.
    """


def test_client_response_is_returned_as_is():
    """Given a stubbed client whose system_one returns a response object, when system_one is called, then that same
    object is returned without transformation or validation.
    """


def test_client_is_created_with_retries_disabled():
    """Given a stubbed TypeSafeClient factory, when system_one is called, then the factory is invoked once with a retry
    policy whose max_retries is 0.
    """


def test_client_is_closed_after_successful_call():
    """Given a stubbed client used as a context manager, when system_one returns normally, then the client context is
    exited exactly once.
    """


def test_provider_failure_propagates_without_retry():
    """Given a stubbed client whose system_one raises RuntimeError("provider unavailable"), when system_one is called,
    then the same error propagates, the client call count is 1, and the client context is exited once.
    """


def test_typesafe_errors_are_not_caught_or_wrapped():
    """Given a stubbed client that raises a TypeSafeError, when system_one is called, then the TypeSafeError reaches
    the caller unchanged so run.audit_batch can record it as a scoped failure.
    """
