import requests

from square_database_helper.configuration import config_str_square_database_ip, config_str_square_database_protocol, \
    config_int_square_database_port


class SquareDatabaseHelper:
    def __init__(self):
        try:
            self.global_str_square_database_url_base = \
                f"{config_str_square_database_protocol}://{config_str_square_database_ip}:{config_int_square_database_port}"
        except Exception:
            raise

    def _make_request(self, method, endpoint, data=None):
        try:
            url = f"{self.global_str_square_database_url_base}/{endpoint}"
            response = requests.request(method, url, json=data)
            response.raise_for_status()
            return response.json()
        except Exception:
            raise

    def insert_rows(self, data: list[dict], database_name: str, schema_name: str, table_name: str):
        try:
            endpoint = "insert_rows"
            payload = {
                "data": data,
                "database_name": database_name,
                "schema_name": schema_name,
                "table_name": table_name
            }
            return self._make_request("POST", endpoint, payload)
        except Exception:
            raise

    def get_rows(self, filters: dict, database_name: str, schema_name: str, table_name: str):
        try:
            endpoint = "get_rows"
            payload = {
                "filters": filters,
                "database_name": database_name,
                "schema_name": schema_name,
                "table_name": table_name
            }
            return self._make_request("POST", endpoint, payload)
        except Exception:
            raise

    def edit_rows(self, data: dict, filters: dict, database_name: str, schema_name: str, table_name: str):
        try:
            endpoint = "edit_rows"
            payload = {
                "data": data,
                "filters": filters,
                "database_name": database_name,
                "schema_name": schema_name,
                "table_name": table_name
            }
            return self._make_request("PUT", endpoint, payload)
        except Exception:
            raise

    def delete_rows(self, filters: dict, database_name: str, schema_name: str, table_name: str):
        try:
            endpoint = "delete_rows"
            payload = {
                "filters": filters,
                "database_name": database_name,
                "schema_name": schema_name,
                "table_name": table_name
            }
            return self._make_request("DELETE", endpoint, payload)
        except Exception:
            raise
