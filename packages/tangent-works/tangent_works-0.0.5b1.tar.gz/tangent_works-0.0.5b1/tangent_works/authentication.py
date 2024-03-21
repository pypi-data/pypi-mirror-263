from typing import Optional

from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient


class TIMLicense:
    _jwt_token: Optional[str] = None

    @property
    def token(self) -> str:
        if self._jwt_token is None:
            raise ValueError('License not set')

        return self._jwt_token

    @token.setter
    def _token(self, value: str) -> None:
        self._jwt_token = value


class DirectLicense(TIMLicense):
    def __init__(self, license_token: str):
        self._token = license_token


class AzureKeyVaultLicense(TIMLicense):
    def __init__(
        self,
        azure_tenant_id: str,
        azure_client_id: str,
        azure_client_secret: str,
        azure_key_vault_name: str,
        azure_secret_name: str,
        azure_key_vault_url: Optional[str] = None
    ):
        credential = ClientSecretCredential(
            tenant_id=azure_tenant_id,
            client_id=azure_client_id,
            client_secret=azure_client_secret
        )
        secret_client = SecretClient(
            vault_url=azure_key_vault_url if azure_key_vault_url is not None else f"https://{azure_key_vault_name}.vault.azure.net/",
            credential=credential
        )
        retrieved_secret = secret_client.get_secret(azure_secret_name)
        self._token = retrieved_secret.value
