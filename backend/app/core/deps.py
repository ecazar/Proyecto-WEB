from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, jwk
from jose.utils import base64url_decode
from jose.exceptions import JWTError
from app.core.config import settings
import requests

def get_signing_key_from_jwks(token_kid, jwks_url):
    import requests
    from jose.utils import base64url_decode
    from jose import jwk

    jwks = requests.get(jwks_url).json()

    for key in jwks["keys"]:
        if key["kid"] == token_kid and key["use"] == "sig" and key["alg"] == "RS256":
            return jwk.construct({
                "kty": key["kty"],
                "e": key["e"],
                "n": key["n"],
                "alg": "RS256"
            }, algorithm="RS256")
    
    raise Exception("No se encontró una clave válida para verificar el token")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.keycloak_url}/protocol/openid-connect/token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        token_kid = jwt.get_unverified_header(token)["kid"]
        public_key = get_signing_key_from_jwks(token_kid, "http://localhost:8080/realms/biblioteca/protocol/openid-connect/certs")
        payload = jwt.decode(token, public_key, algorithms=["RS256"], audience="biblioteca-api")
        # puedes extraer "preferred_username", "sub", "email", etc.
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")