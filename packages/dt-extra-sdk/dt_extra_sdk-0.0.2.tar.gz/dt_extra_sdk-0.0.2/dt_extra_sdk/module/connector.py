from typing import List, Union
import json

from aiohttp import ClientSession

from dt_extra_sdk.module.error import (
    CoreDataError,
    InternalServerError,
    InvalidDataError,
    InvalidTokenError,
)
from dt_extra_sdk.module.kit import encrypt, decrypt
from dt_extra_sdk.module.model import UserModel, CompanyModel, ProjectModel

HANDSHAKE_URI = "/api/extra/handshake"
DATA_URI = "/api/extra/data"
USER_URI = "/api/extra/user_list"
PROJECT_URI = "/api/extra/project"
COMPANY_URI = "/api/extra/company"
AUTH_URI = "/api/extra/auth"
RBAC_URI = "/api/extra/rbac"


class CoreConnector:
    """
    If token is invalid, raise Exception
    """

    def __init__(self, plugin_name: str, secret_key: str, core_address: str):
        self._plugin_name = plugin_name
        self._secret_key = secret_key
        self._core_address = core_address

    async def handshake(self):
        """better call this method before using the connector, raise error if failed to handshake"""
        await self._get_response(plugin_name=self._plugin_name, uri=HANDSHAKE_URI)

    async def auth_check(self, token: str) -> UserModel:
        data = await self._get_response(token=token, uri=AUTH_URI)
        if not isinstance(data, dict):
            raise InvalidDataError(
                f"Invalid auth data detected, expect dict, got: {str(type(data))}"
            )

        return UserModel().parse_dict(data)

    async def rbac_check(self, token: str, project_id: int, endpoint: str):
        data = await self._get_response(
            token=token, project_id=project_id, uri=RBAC_URI, endpoint=endpoint
        )
        if not isinstance(data, dict):
            raise InvalidDataError(
                f"Invalid auth data detected, expect dict, got: {str(type(data))}"
            )

        return UserModel().parse_dict(data)

    async def get_user(self, ids: List[int]) -> List[UserModel]:
        """ignore invalid ids"""
        data_list = await self._get_response(ids=ids, uri=USER_URI)
        if not isinstance(data_list, list):
            raise InvalidDataError(
                f"Invalid user data type detected, expect list, got: {str(type(data_list))}"
            )

        return [UserModel().parse_dict(data) for data in data_list]

    async def get_company(self, company_id: int) -> CompanyModel:
        data = await self._get_response(company_id=company_id, uri=COMPANY_URI)
        if not isinstance(data, dict):
            raise InvalidDataError(
                f"Invalid company data detected, expect dict, got: {str(type(data))}"
            )

        return CompanyModel().parse_dict(data)

    async def get_project(self, app_id: str) -> ProjectModel:
        data = await self._get_response(app_id=app_id, uri=PROJECT_URI)
        if not isinstance(data, dict):
            raise InvalidDataError(
                f"Invalid project data detected, expect dict, got: {str(type(data))}"
            )
        return ProjectModel().parse_dict(data)

    async def _get_response(self, uri: str = DATA_URI, **kwargs) -> Union[dict, None]:
        try:
            encrypted_data = encrypt(self._secret_key, json.dumps(kwargs))
        except Exception:
            raise InvalidDataError("Payload can't be jsonified or encrypted")
        async with ClientSession() as session:
            async with session.post(
                self._core_address + uri, data=encrypted_data
            ) as resp:
                resp_body = await resp.read()
                try:
                    data = decrypt(self._secret_key, resp_body)
                except Exception:
                    raise InvalidDataError(
                        "Resp data can't be decrypted, check if your secret_key is correct"
                    )

                if resp.status in [403, 401]:
                    raise InvalidTokenError("Rbac check failed or token is invalid")
                elif resp.status == 400:
                    raise CoreDataError(
                        "There is something wrong with this user's data"
                    )
                elif resp.status != 200:
                    raise InternalServerError(
                        f"Core server error, status code: {resp.status}"
                    )
                else:
                    try:
                        json_data = json.loads(data)
                        return json_data
                    except json.JSONDecodeError:
                        raise InvalidDataError("Resp data can't be jsonified")
