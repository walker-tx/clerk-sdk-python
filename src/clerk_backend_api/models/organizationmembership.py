"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import Any, Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class OrganizationMembershipObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    ORGANIZATION_MEMBERSHIP = "organization_membership"

class OrganizationMembershipOrganizationObject(str, Enum):
    ORGANIZATION = "organization"

class OrganizationMembershipOrganizationTypedDict(TypedDict):
    object: OrganizationMembershipOrganizationObject
    id: str
    name: str
    slug: str
    max_allowed_memberships: int
    public_metadata: Dict[str, Any]
    private_metadata: Dict[str, Any]
    created_at: int
    r"""Unix timestamp of creation.

    """
    updated_at: int
    r"""Unix timestamp of last update.

    """
    members_count: NotRequired[Nullable[int]]
    admin_delete_enabled: NotRequired[bool]
    created_by: NotRequired[str]
    

class OrganizationMembershipOrganization(BaseModel):
    object: OrganizationMembershipOrganizationObject
    id: str
    name: str
    slug: str
    max_allowed_memberships: int
    public_metadata: Dict[str, Any]
    private_metadata: Dict[str, Any]
    created_at: int
    r"""Unix timestamp of creation.

    """
    updated_at: int
    r"""Unix timestamp of last update.

    """
    members_count: OptionalNullable[int] = UNSET
    admin_delete_enabled: Optional[bool] = None
    created_by: Optional[str] = None
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["members_count", "admin_delete_enabled", "created_by"]
        nullable_fields = ["members_count"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        

class PublicUserDataTypedDict(TypedDict):
    user_id: NotRequired[str]
    first_name: NotRequired[Nullable[str]]
    last_name: NotRequired[Nullable[str]]
    profile_image_url: NotRequired[Nullable[str]]
    image_url: NotRequired[str]
    has_image: NotRequired[bool]
    identifier: NotRequired[Nullable[str]]
    

class PublicUserData(BaseModel):
    user_id: Optional[str] = None
    first_name: OptionalNullable[str] = UNSET
    last_name: OptionalNullable[str] = UNSET
    profile_image_url: Annotated[OptionalNullable[str], pydantic.Field(deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.")] = UNSET
    image_url: Optional[str] = None
    has_image: Optional[bool] = None
    identifier: OptionalNullable[str] = UNSET
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["user_id", "first_name", "last_name", "profile_image_url", "image_url", "has_image", "identifier"]
        nullable_fields = ["first_name", "last_name", "profile_image_url", "identifier"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        

class OrganizationMembershipTypedDict(TypedDict):
    r"""Hello world"""
    
    id: NotRequired[str]
    object: NotRequired[OrganizationMembershipObject]
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    role: NotRequired[str]
    role_name: NotRequired[str]
    permissions: NotRequired[List[str]]
    public_metadata: NotRequired[Dict[str, Any]]
    r"""Metadata saved on the organization membership, accessible from both Frontend and Backend APIs"""
    private_metadata: NotRequired[Dict[str, Any]]
    r"""Metadata saved on the organization membership, accessible only from the Backend API"""
    organization: NotRequired[OrganizationMembershipOrganizationTypedDict]
    public_user_data: NotRequired[PublicUserDataTypedDict]
    created_at: NotRequired[int]
    r"""Unix timestamp of creation."""
    updated_at: NotRequired[int]
    r"""Unix timestamp of last update."""
    

class OrganizationMembership(BaseModel):
    r"""Hello world"""
    
    id: Optional[str] = None
    object: Optional[OrganizationMembershipObject] = None
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    role: Optional[str] = None
    role_name: Optional[str] = None
    permissions: Optional[List[str]] = None
    public_metadata: Optional[Dict[str, Any]] = None
    r"""Metadata saved on the organization membership, accessible from both Frontend and Backend APIs"""
    private_metadata: Optional[Dict[str, Any]] = None
    r"""Metadata saved on the organization membership, accessible only from the Backend API"""
    organization: Optional[OrganizationMembershipOrganization] = None
    public_user_data: Optional[PublicUserData] = None
    created_at: Optional[int] = None
    r"""Unix timestamp of creation."""
    updated_at: Optional[int] = None
    r"""Unix timestamp of last update."""
    
