from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.exceptions import RequestValidationError, HTTPException
from dragons96_tools.models import R
from loguru import logger


def wrapper_exception_handler(app: FastAPI) -> FastAPI:
    """
    给FastAPI对象增加通用依赖处理
    """
    @app.exception_handler(RequestValidationError)
    async def request_validation_exception_handler(request, exc: RequestValidationError):
        logger.error('发生请求参数校验异常, {}', exc)
        return PlainTextResponse(R.fail(msg=str(exc)).model_dump_json())

    @app.exception_handler(AssertionError)
    async def assert_exception_handler(request, exc):
        logger.error('发生断言异常, {}', exc)
        return PlainTextResponse(R.fail(msg=str(exc)).model_dump_json())

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request, exc: HTTPException):
        logger.error('发生http异常, {}', exc)
        return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

    @app.exception_handler(Exception)
    async def exception_handler(request, exc):
        logger.error('发生未知异常, {}', exc)
        return PlainTextResponse(R.fail(msg=str(exc)).model_dump_json())

    return app

