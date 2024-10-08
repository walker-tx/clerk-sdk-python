"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import TypedDict
from typing_extensions import NotRequired


class UpdateInstanceAuthConfigRequestBodyTypedDict(TypedDict):
    restricted_to_allowlist: NotRequired[Nullable[bool]]
    r"""Whether sign up is restricted to email addresses, phone numbers and usernames that are on the allowlist."""
    from_email_address: NotRequired[Nullable[str]]
    r"""The local part of the email address from which authentication-related emails (e.g. OTP code, magic links) will be sent.
    Only alphanumeric values are allowed.
    Note that this value should contain only the local part of the address (e.g. `foo` for `foo@example.com`).
    """
    progressive_sign_up: NotRequired[Nullable[bool]]
    r"""Enable the Progressive Sign Up algorithm. Refer to the [docs](https://clerk.com/docs/upgrade-guides/progressive-sign-up) for more info."""
    session_token_template: NotRequired[Nullable[str]]
    r"""The name of the JWT Template used to augment your session tokens. To disable this, pass an empty string."""
    enhanced_email_deliverability: NotRequired[Nullable[bool]]
    r"""The \"enhanced_email_deliverability\" feature will send emails from \"verifications@clerk.dev\" instead of your domain.
    This can be helpful if you do not have a high domain reputation.
    """
    test_mode: NotRequired[Nullable[bool]]
    r"""Toggles test mode for this instance, allowing the use of test email addresses and phone numbers.
    Defaults to true for development instances.
    """


class UpdateInstanceAuthConfigRequestBody(BaseModel):
    restricted_to_allowlist: OptionalNullable[bool] = False
    r"""Whether sign up is restricted to email addresses, phone numbers and usernames that are on the allowlist."""

    from_email_address: OptionalNullable[str] = UNSET
    r"""The local part of the email address from which authentication-related emails (e.g. OTP code, magic links) will be sent.
    Only alphanumeric values are allowed.
    Note that this value should contain only the local part of the address (e.g. `foo` for `foo@example.com`).
    """

    progressive_sign_up: OptionalNullable[bool] = UNSET
    r"""Enable the Progressive Sign Up algorithm. Refer to the [docs](https://clerk.com/docs/upgrade-guides/progressive-sign-up) for more info."""

    session_token_template: OptionalNullable[str] = UNSET
    r"""The name of the JWT Template used to augment your session tokens. To disable this, pass an empty string."""

    enhanced_email_deliverability: OptionalNullable[bool] = UNSET
    r"""The \"enhanced_email_deliverability\" feature will send emails from \"verifications@clerk.dev\" instead of your domain.
    This can be helpful if you do not have a high domain reputation.
    """

    test_mode: OptionalNullable[bool] = UNSET
    r"""Toggles test mode for this instance, allowing the use of test email addresses and phone numbers.
    Defaults to true for development instances.
    """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "restricted_to_allowlist",
            "from_email_address",
            "progressive_sign_up",
            "session_token_template",
            "enhanced_email_deliverability",
            "test_mode",
        ]
        nullable_fields = [
            "restricted_to_allowlist",
            "from_email_address",
            "progressive_sign_up",
            "session_token_template",
            "enhanced_email_deliverability",
            "test_mode",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
