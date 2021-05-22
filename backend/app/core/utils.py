import logging
import emails

from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Optional, Dict

from emails.template import JinjaTemplate
from jose import jwt
from pydantic.networks import EmailStr

from app.core.config import settings


async def _open_file(path) -> str:
    with open(path) as f:
        return f.read()

async def send_email(
    email_to: EmailStr,
    subject_template: str = "",
    html_template: str = "",
    env: Dict[str, Any] = {},
) -> None:
    assert settings.EMAILS_ENABLED, "no provided configuration for email variables"
    message = emails.Message(
        subject=JinjaTemplate(subject_template),
        html=JinjaTemplate(html_template),
        mail_from=(settings.EMAILS_FROM_NAME, settings.EMAILS_FROM_EMAIL)
    )
    smtp_options = {"host": settings.SMTP_HOST, "port": settings.SMTP_PORT}
    if settings.SMTP_TLS:
        smtp_options["tls"] = True
    if settings.SMTP_USER:
        smtp_options["user"] = settings.SMTP_USER
    if settings.SMTP_PASSWORD:
        smtp_options["password"] = settings.SMTP_PASSWORD
    response = message.send(to=email_to, render=env, smtp=smtp_options)
    logging.info(f"send email result: {response}")

async def send_test_email(email_to: EmailStr) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Test email"
    template_str = await _open_file(Path(settings.EMAIL_TEMPLATE_DIR) / "test_email.html")
    await send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        env={
            "project_name": settings.PROJECT_NAME,
            "email": email_to,
        },
    )

async def send_reset_password_email(
    email_to: EmailStr,
    email: EmailStr,
    token: str
) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Password recovery for user {email}"
    template_str = await _open_file(Path(settings.EMAIL_TEMPLATE_DIR) / "reset_password.html")
    server_host = settings.SERVER_HOST
    link = f"{server_host}/reset_password?token={token}"
    await send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        env={
            "project_name": settings.PROJECT_NAME,
            "username": email,
            "email": email_to,
            "valid_hours": settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS,
            "link": link,
        },
    )

async def send_new_account_email(email_to: EmailStr, username: str, password: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - New account for user {username}"
    template_str = await _open_file(Path(settings.EMAIL_TEMPLATE_DIR) / "new_account.html")
    link = settings.SERVER_HOST
    await send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        env={
            "project_name": settings.PROJECT_NAME,
            "username": username,
            "password": password,
            "email_to": email_to,
            "link": link,
        },
    )

async def generate_password_reset_token(email: EmailStr) -> str:
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encode_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email}, settings.SECRET_KEY, algorithm="HS256",
    )
    return encode_jwt

async def verify_password_reset_token(token: str) -> Optional[str]:
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithm=["HS256"])
        return decoded_token["email"]
    except jwt.JWTError:
        return None
