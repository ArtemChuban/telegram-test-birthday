import http
from urllib.parse import unquote

from fastapi import Depends, HTTPException
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBase
from telegram_webapp_auth.auth import TelegramAuthenticator, generate_secret_key
from telegram_webapp_auth.data import WebAppUser
from telegram_webapp_auth.errors import InvalidInitDataError

from app.settings import settings

telegram_authentication_schema = HTTPBase(scheme="bearer")


def get_telegram_authenticator() -> TelegramAuthenticator:
    secret_key = generate_secret_key(settings.bot.token)
    return TelegramAuthenticator(secret_key)


def get_current_user(
    auth_cred: HTTPAuthorizationCredentials = Depends(telegram_authentication_schema),
    telegram_authenticator: TelegramAuthenticator = Depends(get_telegram_authenticator),
) -> WebAppUser:
    """
    Retrieve the current user based on the provided Telegram authentication credentials.

    This function validates the authentication credentials using the Telegram authenticator.
    If the credentials are valid and the user is found, the corresponding user object is returned.
    If the credentials are invalid or the user is not found, appropriate HTTP exceptions are raised.

    Args:
        auth_cred (HTTPAuthorizationCredentials): The authentication credentials extracted from the request.
        telegram_authenticator (TelegramAuthenticator): The Telegram authenticator used to validate the credentials.

    Raises:
        HTTPException:
            - If the authentication credentials are invalid or cannot be processed, a 403 Forbidden error is raised.
            - If an internal error occurs during validation, a 500 Internal Server Error is raised.

    Returns:
        WebAppUser: The authenticated user object associated with the provided credentials.
    """
    try:
        init_data = telegram_authenticator.validate(unquote(auth_cred.credentials))
    except InvalidInitDataError:
        raise HTTPException(
            status_code=http.HTTPStatus.FORBIDDEN,
            detail="Forbidden access.",
        )
    except Exception:
        raise HTTPException(
            status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,
            detail="Internal error.",
        )

    if init_data.user is None:
        raise HTTPException(
            status_code=http.HTTPStatus.FORBIDDEN,
            detail="Forbidden access.",
        )

    return init_data.user
