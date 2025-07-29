from fastapi import APIRouter, HTTPException
import requests
from pydantic import BaseModel
from app.core.config import settings

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(credentials: LoginRequest):
    print(">> Username recibido:", credentials.username)
    print(">> Password recibido:", credentials.password)

    token_url = f"{settings.keycloak_url}/realms/{settings.keycloak_realm}/protocol/openid-connect/token"
    
    data = {
        "grant_type": "password",
        "client_id": settings.keycloak_client_id,
        "client_secret": settings.keycloak_client_secret,
        "username": credentials.username.strip(),
        "password": credentials.password
    }

    resp = requests.post(token_url, data=data)
    print(">> Status Keycloak:", resp.status_code)
    print(">> Respuesta Keycloak:", resp.text)

    if resp.status_code != 200:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    return resp.json()
