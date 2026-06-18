# gemini_utils.py

import json
import time
from collections import deque

from google import genai
from google.genai import types

from schemas import RESPONSE_SCHEMA, ANSWER_SCHEMA
from prompts import (
    build_question_prompt,
    build_answer_prompt,
)


class RateLimiter:
    """
    Sliding-window rate limiter.
    """

    def __init__(self, max_per_minute: int):
        self.max_per_minute = max_per_minute
        self.timestamps = deque()

    def wait(self):
        now = time.monotonic()

        while self.timestamps and now - self.timestamps[0] >= 60:
            self.timestamps.popleft()

        if len(self.timestamps) >= self.max_per_minute:

            sleep_time = 60 - (now - self.timestamps[0]) + 0.05

            if sleep_time > 0:
                time.sleep(sleep_time)

            now = time.monotonic()

            while self.timestamps and now - self.timestamps[0] >= 60:
                self.timestamps.popleft()

        self.timestamps.append(time.monotonic())


def create_client():
    """
    Create Gemini client.

    Reads GEMINI_API_KEY automatically from environment.
    """

    return genai.Client()


max_retries = 5
DEFAULT_MODEL = "gemini-3.1-flash-lite"


def call_gemini(
    prompt=None,
    *,
    client=None,
    model=None,
    response_schema=None,
    rate_limiter=None,
    pdf_bytes=None,
):
    """
    Generic Gemini call with retries.
    """

    if prompt is None:
        raise TypeError("call_gemini() missing required argument: 'prompt'")

    if (
        client is None
        and model is None
        and response_schema is None
        and rate_limiter is None
    ):
        client = create_client()
        model = DEFAULT_MODEL

        for attempt in range(1, max_retries + 1):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        temperature=0.1,
                        max_output_tokens=65536,
                    ),
                )

                print("Output chars:", len(response.text))
                return response.text

            except Exception as e:
                print(f"    [warn] attempt {attempt}/{max_retries} failed: {e}")

                if attempt < max_retries:
                    time.sleep(5 * attempt)

        return None

    if (
        client is None
        or model is None
        or response_schema is None
        or rate_limiter is None
    ):
        raise TypeError(
            "call_gemini() requires client, model, response_schema, and rate_limiter when using the structured API"
        )

    for attempt in range(1, max_retries + 1):

        rate_limiter.wait()

        try:

            response = client.models.generate_content(
                model=model,
                contents=[
                    types.Part.from_bytes(
                        data=pdf_bytes,
                        mime_type="application/pdf",
                    ),
                    prompt,
                ],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=response_schema,
                    temperature=0.1,
                    max_output_tokens=65536,
                ),
            )
            # print(response.text)
            print("Output chars:", len(response.text))

            return json.loads(response.text)

        except Exception as e:

            print(f"    [warn] attempt {attempt}/{max_retries} failed: {e}")

            if attempt < max_retries:
                time.sleep(5 * attempt)

    return None


def call_gemini_text(
    *,
    client,
    model,
    prompt,
    response_schema,
    rate_limiter,
    temperature=0.1,
    temperature_escalation=0.3,
    validate=None,
):
    """
    validate: optional callable(result) -> None. Raise inside it (or let
    a KeyError/etc propagate) to signal "parsed fine but content is wrong"
    (e.g. wrong item count). Treated the same as a parse failure: retried
    with escalating temperature, since a fixed low temperature tends to
    reproduce the same degenerate repetition loop on retry rather than
    recovering from it.
    """
    for attempt in range(1, max_retries + 1):

        rate_limiter.wait()

        current_temperature = min(
            temperature + temperature_escalation * (attempt - 1),
            1.0,
        )

        try:

            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=response_schema,
                    temperature=current_temperature,
                    max_output_tokens=65536,
                ),
            )

            print(
                "Output chars:",
                len(response.text),
                f"(temperature={current_temperature:.2f})",
            )

            try:

                result = json.loads(response.text)

            except Exception:

                with open(
                    f"bad_response_attempt{attempt}.json",
                    "w",
                    encoding="utf-8",
                ) as f:

                    f.write(response.text)

                raise

            if validate is not None:
                validate(result)

            return result

        except Exception as e:

            print(f"    [warn] attempt {attempt}/{max_retries} failed: {e}")

            if attempt < max_retries:

                time.sleep(5 * attempt)

    return None


def extract_question_batch(
    client,
    model: str,
    pdf_bytes: bytes,
    start_page: int,
    end_page: int,
    rate_limiter: RateLimiter,
):
    """
    Extract one question batch.
    """

    prompt = build_question_prompt(
        start_page,
        end_page,
    )

    result = call_gemini(
        client=client,
        model=model,
        pdf_bytes=pdf_bytes,
        prompt=prompt,
        response_schema=RESPONSE_SCHEMA,
        rate_limiter=rate_limiter,
    )

    if result is None:
        return None

    return result


def extract_answer_batch(
    client,
    model: str,
    pdf_bytes: bytes,
    missing_question_numbers: list[str],
    rate_limiter: RateLimiter,
):
    """
    Extract answers for a batch of question numbers.
    """

    prompt = build_answer_prompt(missing_question_numbers)

    result = call_gemini(
        client=client,
        model=model,
        pdf_bytes=pdf_bytes,
        prompt=prompt,
        response_schema=ANSWER_SCHEMA,
        rate_limiter=rate_limiter,
    )

    if result is None:
        return None

    return result


def extract_questions(
    client,
    model: str,
    pdf_bytes: bytes,
    start_page: int,
    end_page: int,
    rate_limiter: RateLimiter,
):
    """
    Convenience wrapper.

    Returns list of questions.
    """

    result = extract_question_batch(
        client=client,
        model=model,
        pdf_bytes=pdf_bytes,
        start_page=start_page,
        end_page=end_page,
        rate_limiter=rate_limiter,
    )

    if result is None:
        return []

    return result.get("questions", [])


def extract_answers(
    client,
    model: str,
    pdf_bytes: bytes,
    missing_question_numbers: list[str],
    rate_limiter: RateLimiter,
):
    """
    Convenience wrapper.

    Returns list of answers.
    """

    result = extract_answer_batch(
        client=client,
        model=model,
        pdf_bytes=pdf_bytes,
        missing_question_numbers=missing_question_numbers,
        rate_limiter=rate_limiter,
    )

    if result is None:
        return []

    return result.get("answers", [])
