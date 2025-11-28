from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import BaseModel, EmailStr
from typing import List
from security import config_data
from dotenv import load_dotenv

load_dotenv(".env")


conf = ConnectionConfig(
    MAIL_USERNAME=config_data.get("MAIL_USERNAME"),
    MAIL_PASSWORD=config_data.get("MAIL_PASSWORD"),
    MAIL_FROM=config_data.get("MAIL_FROM"),
    MAIL_PORT=config_data.get("MAIL_PORT"),
    MAIL_SERVER=config_data.get("MAIL_SERVER"),
    MAIL_STARTTLS=config_data.get("MAIL_STARTTLS"),
    MAIL_SSL_TLS=config_data.get("MAIL_SSL_TLS"),
    USE_CREDENTIALS=config_data.get("USE_CREDENTIALS"),
    VALIDATE_CERTS=config_data.get("VALIDATE_CERTS")
)

front_base_url = config_data.get("FRONT_BASE_URL")
front_account_verification_url = config_data.get("FRONT_ACCOUNT_VERIFICATION_URL")
front_password_reset_url = config_data.get("FRONT_PASSWORD_RESET_URL")


class EmailSchema(BaseModel):
    email: List[EmailStr]


async def send_verification_email(username: str, email: EmailSchema, token: str):

    template = f"""
        <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Confirmation d'Inscription</title>
                <!-- Inclure Bootstrap CSS -->
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
                <style>
                    body {{
                        background-color: #faf4f4;
                    }}
                    .btn:hover {{
                        opacity: 3;
                        animation: heartBeat ;
                        animation-duration: 2s;
                    }}
                </style>
            </head>
            <body>

                <div class="container" style="max-width: 600px; margin: auto; padding: 20px;margin-top:5%;">
                    <div class="text-center mb-5">
                        <h2>Vérification d'Inscription</h2>
                    </div>
                    <div class="card" style="background-color: #ffffff; border-radius: 8px; box-shadow:5px 15px 10px 10px rgba(0,0,0,0.1); padding: 20px;">
                        <p>Bonjour <strong>{username},</strong></p>
                        <p>Merci de vous être inscrit à notre service de boutique en ligne K-store. Pour finaliser votre inscription, veuillez cliquer sur le lien de vérification ci-dessous :</p>
                        <p class="text-center"><a href="{front_base_url}{front_account_verification_url}?token={token}" style="background-color: #264a67; opacity: 0.8; text-decoration: none; color: white; padding: 5px;" class="btn text-white p-3">Vérifier</a></p>
                        <p>Merci,<br>Votre Équipe, <strong>KAPITAL DEV</strong></p>
                    </div>

                </div>

            </body>
            </html>

    """


    message = MessageSchema(
        subject="KAPITAL DEV - Vérification de compte.",
        recipients=email, #Liste des destinataires. Ici, un seul.
        body=template,
        subtype=MessageType.html
    )


    the_email = FastMail(conf)
    await the_email.send_message(message=message)

    return token


async def resend_verification_email(username: str, email: EmailSchema, token: str):
    template = f"""
        <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Confirmation d'Inscription</title>
                <!-- Inclure Bootstrap CSS -->
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
                <style>
                    body {{
                        background-color: #faf4f4;
                    }}
                    .btn:hover {{
                        opacity: 3;
                        animation: heartBeat ;
                        animation-duration: 2s;
                    }}
                </style>
            </head>
            <body>

                <div class="container" style="max-width: 600px; margin: auto; padding: 20px;margin-top:5%;">
                    <div class="text-center mb-5">
                        <h2>Nouveau lien de vérification d'email</h2>
                    </div>
                    <div class="card" style="background-color: #ffffff; border-radius: 8px; box-shadow:5px 15px 10px 10px rgba(0,0,0,0.1); padding: 20px;">
                        <p>Bonjour <strong>{username},</strong></p>
                        <p>Merci de vous être inscrit à notre service de boutique en ligne K-store. Voici votre nouveau lien de vérification de votre email :</p>
                        <p class="text-center"><a href="{front_base_url}{front_account_verification_url}?token={token}" style="background-color: #264a67; opacity: 0.8; text-decoration: none; color: white; padding: 5px;" class="btn text-white p-3">Vérifier</a></p>
                        <p>Merci,<br>Votre Équipe, <strong>KAPITAL DEV</strong></p>
                    </div>

                </div>

            </body>
            </html>

    """

    message = MessageSchema(
        subject="KAPITAL DEV - Vérification de compte.",
        recipients=email,  # Liste des destinataires. Ici, un seul.
        body=template,
        subtype=MessageType.html
    )

    the_email = FastMail(conf)
    await the_email.send_message(message=message)

    return token

async def send_reset_password_email(username: str, email: EmailSchema, token: str):
    template = f"""
        <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Réinitialisation de Mot de Passe</title>
                <!-- Inclure Bootstrap CSS -->
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
                <style>
                    body {{
                        background-color: #faf4f4;
                        text-align: justify;
                    }}
                    .btn:hover{{
                        opacity: 3;
                        animation: pulse;
                        animation-duration: 2s;
                    }}
                </style>
            </head>
            <body>

                <div class="container" style="max-width: 600px; margin: auto; padding: 20px;margin-top:10%;">
                    <div class="text-center mb-5">
                        <h2>Réinitialisation de Mot de Passe</h2>
                    </div>
                    <div class="card" style="background-color: #ffffff; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); padding: 20px;">
                        <p>Bonjour <strong>{username},</strong></p>
                        <p>Pour réinitialiser votre mot de passe, veuillez cliquer sur le lien ci-dessous:</p>
                        <p class="text-center"><a href="{front_base_url}{front_password_reset_url}?token={token}" style="background-color: #264a67; opacity: 0.8; text-decoration: none; color: white; padding: 5px;" class="btn text-white p-3">Réinitialiser</a></p>
                        <p>Merci,<br>Votre Équipe <strong>KAPITAL DEV</strong></p>
                    </div>
                </div>

            </body>
            </html>
    """


    message = MessageSchema(
        subject="KAPITAL DEV - Réinitialisation de mot de passe.",
        recipients=email,  # Liste des destinataires. Ici, un seul.
        body=template,
        subtype=MessageType.html
    )

    the_email = FastMail(conf)
    await the_email.send_message(message=message)

    return token
