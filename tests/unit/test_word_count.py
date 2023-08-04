import logging
from http import HTTPStatus

import azure.functions as func
from pytest import LogCaptureFixture

import word_count


def test_app_should_calculate_correct_word_count() -> None:
    request = func.HttpRequest(
        method="GET",
        body=bytes(),
        url="api/word_count",
        params={"words": "This is a test sting"},
    )
    response = word_count.main(request)
    body = response.get_body()

    assert response.status_code == HTTPStatus.OK
    assert body == b"String 'words' contains 5 words"


def test_app_should_log_info_when_call_successful(caplog: LogCaptureFixture) -> None:
    caplog.set_level(logging.INFO)

    request = func.HttpRequest(
        method="GET",
        body=bytes(),
        url="api/word_count",
        params={"words": "This is a test sting"},
    )
    word_count.main(request)

    assert "Executing function 'word_count'" in caplog.text


def test_app_should_return_error_when_words_not_provided() -> None:
    request = func.HttpRequest(
        method="GET",
        body=bytes(),
        url="api/word_count",
        params={},
    )
    response = word_count.main(request)
    body = response.get_body()

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert body == b"Request parameter 'words' not provided"


def test_app_log_error_when_words_not_provided(caplog: LogCaptureFixture) -> None:
    caplog.set_level(logging.ERROR)

    request = func.HttpRequest(
        method="GET",
        body=bytes(),
        url="api/word_count",
        params={},
    )
    word_count.main(request)

    assert "Request parameter 'words' not provided" in caplog.text
