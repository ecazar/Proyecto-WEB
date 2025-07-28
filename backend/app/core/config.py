from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    DATABASE_URL: str = Field(..., alias="DATABASE_URL")

    keycloak_url: str = Field(..., alias="KEYCLOAK_URL")
    keycloak_realm: str = Field(..., alias="KEYCLOAK_REALM")
    keycloak_client_secret: str = Field(..., alias="KEYCLOAK_CLIENT_SECRET")
    keycloak_client_id: str = Field(..., alias="KEYCLOAK_CLIENT_ID")
    keycloak_audience: str = Field(..., alias="KEYCLOAK_AUDIENCE")

    model_config = SettingsConfigDict(env_file=".env", extra="allow")

    @property
    def KEYCLOAK_ISSUER(self):
        return f"{self.keycloak_url}/realms/{self.keycloak_realm}"

    @property
    def KEYCLOAK_ALGORITHMS(self):
        return ["RS256"]

settings = Settings()
