from jose import jwt, JWTError
from datetime import datetime,timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv


load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "secret123")
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def decode_access_token(token : str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('email')

        if email is None:
            raise HTTPException(status_code=401, detail='Invalid token')
        return email

    except JWTError:
        raise HTTPException(status_code=401, detail='Invalid or expired token!')


