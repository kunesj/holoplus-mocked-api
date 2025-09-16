from __future__ import annotations

import contextlib
import uuid
from http import HTTPStatus
from typing import Annotated, Iterator, Self, cast

import litestar
import litestar.serialization
import msgspec
from litestar import status_codes
from litestar._openapi.responses import ResponseFactory, pascal_case_to_text
from litestar.enums import MediaType
from litestar.exceptions import HTTPException, NotFoundException, ValidationException
from litestar.openapi.spec import OpenAPIResponse
from litestar.openapi.spec.enums import OpenAPIType
from litestar.openapi.spec.media_type import OpenAPIMediaType
from litestar.openapi.spec.responses import Responses
from litestar.openapi.spec.schema import Schema
from litestar.utils import get_name


class HoloplusException(HTTPException):
    holoplus_code: str = ""
    holoplus_message: str = ""
    holoplus_detail: str = ""
    holoplus_title: str | None = None

    def __init__(
        self,
        *,
        code: str | None = None,
        message: str | None = None,
        detail: str | None = None,
        title: str | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        self.holoplus_code = code or self.holoplus_code
        self.holoplus_message = message or self.holoplus_message
        self.holoplus_detail = detail or self.holoplus_detail
        self.holoplus_title = title or self.holoplus_title

        super().__init__(
            self.holoplus_code,
            self.holoplus_message,
            detail=self.holoplus_detail,
            headers=headers,
            extra={"title": self.holoplus_title},
        )


class HoloplusNotFoundException(HoloplusException):
    status_code = status_codes.HTTP_404_NOT_FOUND  # TODO: verify
    holoplus_code = "E100"
    holoplus_message = (
        "ネットワークの状況をご確認の上、アプリの再起動などをしても改善しない場合は、"
        "「マイページ＞設定・アプリ情報＞お問い合わせ」からお問い合わせください。"
    )
    holoplus_detail = ""
    holoplus_title = "不明なエラーが発生しました😢"


class HoloplusMissingTokenException(HoloplusException):
    status_code = status_codes.HTTP_400_BAD_REQUEST
    holoplus_code = "Bad Request"
    holoplus_message = "Authentication failed😢\nPlease check your internet connection and try again!"
    holoplus_detail = "authorization header is missing"


class ErrorResponse(msgspec.Struct, kw_only=True):
    code: Annotated[str, msgspec.Meta(examples=["Bad Request"])] = msgspec.field()
    message: Annotated[
        str,
        msgspec.Meta(examples=["Authentication failed😢\nPlease check your internet connection and try again!"]),
    ] = msgspec.field()
    detail: Annotated[str, msgspec.Meta(examples=["authorization header is missing"])] = msgspec.field()
    title: Annotated[str | msgspec.UnsetType, msgspec.Meta()] = msgspec.field(default=msgspec.UNSET)

    @classmethod
    def example_from_exception_class(cls, exc: type[Exception]) -> Self:
        if issubclass(exc, HoloplusException):
            return cls(
                code=exc.holoplus_code,
                message=exc.holoplus_message,
                detail=exc.holoplus_detail,
                title=exc.holoplus_title or msgspec.UNSET,
            )
        raise TypeError(exc)


class RootErrorResponse(msgspec.Struct, kw_only=True):
    name: Annotated[str, msgspec.Meta(examples=["fault", "missing_field"])] = msgspec.field()
    id: Annotated[str, msgspec.Meta(examples=["7HSr-dWY", "Dd52rDBj"])] = msgspec.field()
    message: Annotated[
        str,
        msgspec.Meta(
            examples=[
                "404 page not found",
                (
                    '"channel_id" is missing from query string; "limit" is missing from query string; '
                    "limit must be greater or equal than 1 but got value 0"
                ),
            ]
        ),
    ] = msgspec.field()
    temporary: Annotated[bool, msgspec.Meta(examples=[False, False])] = msgspec.field()
    timeout: Annotated[bool, msgspec.Meta(examples=[False, False])] = msgspec.field()
    fault: Annotated[bool, msgspec.Meta(examples=[True, False])] = msgspec.field()

    @classmethod
    def example_from_exception_class(cls, exc: type[Exception]) -> Self:
        if issubclass(exc, NotFoundException):
            return cls(
                name="fault",
                id=uuid.uuid4().hex[:8],
                message="404 page not found",
                temporary=False,
                timeout=False,
                fault=True,
            )

        if issubclass(exc, ValidationException):
            return cls(
                name="missing_field",
                id=uuid.uuid4().hex[:8],
                message='"channel_id" is missing from query string; "limit" is missing from query string; '
                "limit must be greater or equal than 1 but got value 0",
                temporary=False,
                timeout=False,
                fault=False,
            )

        message = ""
        if issubclass(exc, HTTPException):
            exc = cast("type[HTTPException]", exc)
            with contextlib.suppress(Exception):
                message = HTTPStatus(exc.status_code).phrase

            message = getattr(exc, "detail", "") or message

        return cls(
            name="fault",
            id=uuid.uuid4().hex[:8],
            message=message or "error",
            temporary=False,
            timeout=False,
            fault=True,
        )


def root_exception_handler(_: litestar.Request, exc: Exception) -> litestar.Response:
    """
    Error caused by not found endpoint is in different format.
    We will assume that this format is used only by the root app.
    """
    if isinstance(exc, HTTPException):
        message = exc.detail
        status_code = exc.status_code
    else:
        message = str(exc)
        status_code = status_codes.HTTP_500_INTERNAL_SERVER_ERROR

    return litestar.Response(
        media_type=litestar.MediaType.JSON,
        content=RootErrorResponse(
            name="fault",
            id=uuid.uuid4().hex[:8],
            message=message,
            temporary=False,
            timeout=False,
            fault=True,
        ),
        status_code=status_code,
    )


def exception_handler(_: litestar.Request, exc: Exception) -> litestar.Response:
    if isinstance(exc, HoloplusException):
        return litestar.Response(
            media_type=litestar.MediaType.JSON,
            content=ErrorResponse(
                code=exc.holoplus_code,
                message=exc.holoplus_message,
                detail=exc.holoplus_detail,
                title=exc.holoplus_title or msgspec.UNSET,
            ),
            status_code=exc.status_code,
            headers=exc.headers,
        )

    if isinstance(exc, HTTPException):
        return litestar.Response(
            media_type=litestar.MediaType.JSON,
            content=ErrorResponse(
                code=str(exc.status_code),
                message=str(exc.args),
                detail=exc.detail,
                # `title` not set
            ),
            status_code=exc.status_code,
        )

    return litestar.Response(
        media_type=litestar.MediaType.JSON,
        content=ErrorResponse(
            code="Exception",
            message=exc.__class__.__name__,
            detail=str(exc),
            # `title` not set
        ),
        status_code=status_codes.HTTP_500_INTERNAL_SERVER_ERROR,
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

        example: ErrorResponse | RootErrorResponse
        for exc in exception_group:
            if issubclass(exc, HoloplusException):
                required = ["code", "message", "detail"]
                properties = {
                    "code": Schema(type=OpenAPIType.STRING),
                    "message": Schema(type=OpenAPIType.STRING),
                    "detail": Schema(type=OpenAPIType.STRING),
                    "title": Schema(type=OpenAPIType.STRING),
                }
                example = ErrorResponse.example_from_exception_class(exc)
                group_description = example.code

            else:
                required = ["name", "id", "message", "temporary", "timeout", "fault"]
                properties = {
                    "name": Schema(type=OpenAPIType.STRING),
                    "id": Schema(type=OpenAPIType.STRING),
                    "message": Schema(type=OpenAPIType.STRING),
                    "temporary": Schema(type=OpenAPIType.BOOLEAN),
                    "timeout": Schema(type=OpenAPIType.BOOLEAN),
                    "fault": Schema(type=OpenAPIType.BOOLEAN),
                }
                example = RootErrorResponse.example_from_exception_class(exc)

            example_jsonable = litestar.serialization.decode_json(litestar.serialization.encode_json(example))
            exceptions_schemas.append(
                Schema(
                    type=OpenAPIType.OBJECT,
                    required=required,
                    properties=properties,
                    description=pascal_case_to_text(get_name(exc)),
                    examples=[example_jsonable],
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
