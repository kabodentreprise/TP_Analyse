from fastapi import HTTPException
from starlette import status


def raise_exception_for_expired_token():
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
        )


def raise_exception_for_undecodable_token():
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not decode token",
        )


def raise_exception_for_unverifiable_token():
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not verify token",
        )


def raise_exception_for_unknown_token():
    raise HTTPException(status_code=401, detail='Unknown token !')


def raise_exception_for_existing_email():
    raise HTTPException(status_code=401, detail='Email already exists !')


def raise_exception_for_existing_username():
    raise HTTPException(status_code=401, detail='Username already exists !')


def raise_exception_for_invalid_email():
    raise HTTPException(status_code=401, detail='Invalid email !')


def raise_exception_for_unknown_email():
    raise HTTPException(status_code=401, detail='Unknown email !')

def raise_exception_for_weak_password():
    raise HTTPException(status_code=401, detail='Mot de passe faible !')

def raise_exception_for_email_connection_error():
    raise HTTPException(status_code=500, detail='Email sending error. Check credentials or your network !')

def raise_exception_for_invalid_email():
    raise HTTPException(status_code=500, detail='Email sending error. Invalid email address !')


def raise_exception_for_email_already_verified():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already verified !",
                        headers={"WWW.Authenticate": "Bearer"})


def raise_exception_for_non_verified_user():
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User's email not verified yet !")


def raise_exception_for_invalid_login_credentials():
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Email or password incorrect.')


def raise_exception_for_authentication_failed():
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication failed.')


def raise_exception_for_error_occured():
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Une erreur s\'est produite.')
