from dt_extra_sdk.module.connector import CoreConnector

core_connector: CoreConnector


def init_connector(extra_name: str, secret_key: str, core_address: str):
    global core_connector
    core_connector = CoreConnector(extra_name, secret_key, core_address)


def get_connector() -> CoreConnector:
    if not core_connector:
        raise Exception("connector not initialized. Call entry.init() first.")
    return core_connector
