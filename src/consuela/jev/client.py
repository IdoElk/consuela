"""Send one request to Jev through TypeSafe."""

from typesafe_sdk import RetryPolicy, TypeSafeClient


def system_one(state, questions):
    with TypeSafeClient(retry=RetryPolicy(max_retries=0)) as client:
        return client.system_one(state=state, questions=questions)
