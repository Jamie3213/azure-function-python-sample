import logging
from http import HTTPStatus

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Executing function 'word_count'")
    words = req.params.get("words")

    if words is None:
        error_msg = "Request parameter 'words' not provided"
        logging.error(error_msg)
        return func.HttpResponse(error_msg, status_code=HTTPStatus.UNPROCESSABLE_ENTITY)

    word_count = len(words.split())

    return func.HttpResponse(
        f"String 'words' contains {word_count} words", status_code=HTTPStatus.OK
    )
