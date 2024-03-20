from typing import Dict

from dt_extra_sdk.module.error import MissingDataError


class BaseModel:
    def get_dict(self) -> Dict:
        return vars(self)

    def parse_dict(self, data: Dict):
        for attr_name, _ in self.__dict__.items():
            if data.get(attr_name) is None or type(data[attr_name]) != type(
                getattr(self, attr_name)
            ):
                raise MissingDataError("Missing data: " + attr_name)
            setattr(self, attr_name, data[attr_name])
        return self


class UserModel(BaseModel):
    def __init__(self):
        self.id: int = 0
        self.username: str = ""
        self.nickname: str = ""
        self.status: int = -1
        self.deleted: int = -1
        self.company_id: int = -1
        self.lang: str = ""


class CompanyModel(BaseModel):
    def __init__(self):
        self.id: int = 0
        self.name: str = ""
        self.start_service: str = ""
        self.stop_service: str = ""
        self.meta_event_limit: int = 0
        self.access_version: str = ""
        self.report_url: str = ""


class ProjectModel(BaseModel):
    def __init__(self) -> None:
        self.report_url: str = ""
        self.thirdparty_integration_limit: int = 0
        self.time_zone_offset: int = 0
        self.company_id: int = 0
