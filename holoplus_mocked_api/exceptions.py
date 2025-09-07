from __future__ import annotations

import contextlib
import uuid
from http import HTTPStatus
from typing import Annotated, Iterator

import litestar
import msgspec
from litestar._openapi.responses import ResponseFactory, pascal_case_to_text
from litestar.enums import MediaType
from litestar.exceptions import HTTPException, ValidationException
from litestar.openapi.spec import Example, OpenAPIResponse
from litestar.openapi.spec.enums import OpenAPIType
from litestar.openapi.spec.media_type import OpenAPIMediaType
from litestar.openapi.spec.responses import Responses
from litestar.openapi.spec.schema import Schema
from litestar.params import Parameter
from litestar.utils import get_name


class ErrorResponse(msgspec.Struct, kw_only=True):
    code: Annotated[str, Parameter(examples=[Example(value="Bad Request")])] = msgspec.field()
    message: Annotated[
        str,
        Parameter(
            examples=[Example(value="Authentication failed😢\nPlease check your internet connection and try again!")]
        ),
    ] = msgspec.field()
    detail: Annotated[str, Parameter(examples=[Example(value="authorization header is missing")])] = msgspec.field()


class RootErrorResponse(msgspec.Struct, kw_only=True):
    name: Annotated[str, Parameter(examples=[Example(value="fault")])] = msgspec.field()
    id: Annotated[str, Parameter(examples=[Example(value="7HSr-dWY")])] = msgspec.field()
    message: Annotated[str, Parameter(examples=[Example(value="404 page not found")])] = msgspec.field()
    temporary: Annotated[bool, Parameter(examples=[Example(value=False)])] = msgspec.field()
    timeout: Annotated[bool, Parameter(examples=[Example(value=False)])] = msgspec.field()
    fault: Annotated[bool, Parameter(examples=[Example(value=True)])] = msgspec.field()


# TODO: use correct error values
def root_exception_handler(_: litestar.Request, exc: Exception) -> litestar.Response[RootErrorResponse]:
    return litestar.Response(
        media_type=litestar.MediaType.JSON,
        content=RootErrorResponse(
            name="fault",
            id=uuid.uuid4().hex[:8],
            message=exc.detail if isinstance(exc, HTTPException) else str(exc),
            temporary=True,
            timeout=False,
            fault=True,
        ),
        status_code=exc.status_code if isinstance(exc, HTTPException) else 500,
    )


# TODO: use correct error values
def exception_handler(_: litestar.Request, exc: Exception) -> litestar.Response[ErrorResponse]:
    return litestar.Response(
        media_type=litestar.MediaType.JSON,
        content=ErrorResponse(
            code="Exception",
            message=exc.__class__.__name__,
            detail=exc.detail if isinstance(exc, HTTPException) else str(exc),
        ),
        status_code=exc.status_code if isinstance(exc, HTTPException) else 500,
    )


def create_responses(self: ResponseFactory, raises_validation_error: bool) -> Responses | None:
    """
    Patched version of `ResponseFactory.create_responses`
    """
    responses: Responses = {
        str(self.route_handler.status_code): self.create_success_response(),
    }

    exceptions = list(self.route_handler.raises or [])
    if raises_validation_error and ValidationException not in exceptions:
        exceptions.append(ValidationException)

    for status_code, response in create_error_responses(exceptions=exceptions):
        responses[status_code] = response

    for status_code, response in self.create_additional_responses():
        responses[status_code] = response

    return responses or None


def create_error_responses(exceptions: list[type[HTTPException]]) -> Iterator[tuple[str, OpenAPIResponse]]:
    """
    Patched version of `create_error_responses` that uses the correct error format.
    """
    grouped_exceptions: dict[int, list[type[HTTPException]]] = {}
    for exc in exceptions:
        if not grouped_exceptions.get(exc.status_code):
            grouped_exceptions[exc.status_code] = []
        grouped_exceptions[exc.status_code].append(exc)
    for status_code, exception_group in grouped_exceptions.items():
        exceptions_schemas = []
        group_description: str = ""
        for exc in exception_group:
            example_detail = ""
            if hasattr(exc, "detail") and exc.detail:
                group_description = exc.detail
                example_detail = exc.detail

            if not example_detail:
                with contextlib.suppress(Exception):
                    example_detail = HTTPStatus(status_code).phrase

            exceptions_schemas.append(
                Schema(
                    type=OpenAPIType.OBJECT,
                    required=["code", "message", "detail"],
                    properties={
                        "code": Schema(type=OpenAPIType.STRING),
                        "message": Schema(type=OpenAPIType.STRING),
                        "detail": Schema(type=OpenAPIType.STRING),
                    },
                    description=pascal_case_to_text(get_name(exc)),
                    examples=[{"code": example_detail, "message": group_description, "detail": ""}],
                )
            )
        if len(exceptions_schemas) > 1:
            schema = Schema(one_of=exceptions_schemas)
        else:
            schema = exceptions_schemas[0]

        if not group_description:
            with contextlib.suppress(Exception):
                group_description = HTTPStatus(status_code).description

        yield (
            str(status_code),
            OpenAPIResponse(
                description=group_description,
                content={MediaType.JSON: OpenAPIMediaType(schema=schema)},
            ),
        )


def litestar_monkey_patch() -> None:
    ResponseFactory.create_responses = create_responses
