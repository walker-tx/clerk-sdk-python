"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import (
    FieldMetadata,
    MultipartFormMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import io
import pydantic
from typing import IO, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class UploadOrganizationLogoFileTypedDict(TypedDict):
    file_name: str
    content: Union[bytes, IO[bytes], io.BufferedReader]
    content_type: NotRequired[str]


class UploadOrganizationLogoFile(BaseModel):
    file_name: Annotated[
        str, pydantic.Field(alias="file"), FieldMetadata(multipart=True)
    ]

    content: Annotated[
        Union[bytes, IO[bytes], io.BufferedReader],
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(content=True)),
    ]

    content_type: Annotated[
        Optional[str],
        pydantic.Field(alias="Content-Type"),
        FieldMetadata(multipart=True),
    ] = None


class UploadOrganizationLogoRequestBodyTypedDict(TypedDict):
    uploader_user_id: str
    r"""The ID of the user that will be credited with the image upload."""
    file: UploadOrganizationLogoFileTypedDict


class UploadOrganizationLogoRequestBody(BaseModel):
    uploader_user_id: Annotated[str, FieldMetadata(multipart=True)]
    r"""The ID of the user that will be credited with the image upload."""

    file: Annotated[
        UploadOrganizationLogoFile,
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(file=True)),
    ]


class UploadOrganizationLogoRequestTypedDict(TypedDict):
    organization_id: str
    r"""The ID of the organization for which to upload a logo"""
    request_body: NotRequired[UploadOrganizationLogoRequestBodyTypedDict]


class UploadOrganizationLogoRequest(BaseModel):
    organization_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the organization for which to upload a logo"""

    request_body: Annotated[
        Optional[UploadOrganizationLogoRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="multipart/form-data")),
    ] = None
