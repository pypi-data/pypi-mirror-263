from __future__ import annotations

import os
import urllib.parse
from morphdb_utils.type import SqlResultResponse

import pandas as pd
import requests


class MorphApiError(Exception):
    pass


def _read_configuration_from_env() -> dict[str, str]:
    config = {}
    if "MORPH_DATABASE_ID" in os.environ:
        config["database_id"] = os.environ["MORPH_DATABASE_ID"]
    if "MORPH_BASE_URL" in os.environ:
        config["base_url"] = os.environ["MORPH_BASE_URL"]
    if "MORPH_TEAM_SLUG" in os.environ:
        config["team_slug"] = os.environ["MORPH_TEAM_SLUG"]
    if "MORPH_AUTHORIZATION" in os.environ:
        config["authorization"] = os.environ["MORPH_AUTHORIZATION"]
    if "MORPH_NOTEBOOK_ID" in os.environ:
        config["notebook_id"] = os.environ["MORPH_NOTEBOOK_ID"]

    return config


def _canonicalize_base_url(base_url: str) -> str:
    if base_url.startswith("http"):
        return base_url
    else:
        return f"https://{base_url}"


def _convert_sql_engine_response(
    response: SqlResultResponse,
) -> pd.DataFrame:
    fields = response.headers

    def parse_value(case_type, value):
        if case_type == "nullValue":
            return None
        elif case_type == "doubleValue":
            return value[case_type]
        elif case_type == "floatValue":
            return value[case_type]
        elif case_type == "int32Value":
            return value[case_type]
        elif case_type == "int64Value":
            return int(value[case_type])
        elif case_type == "uint32Value":
            return value[case_type]
        elif case_type == "uint64Value":
            return int(value[case_type])
        elif case_type == "sint32Value":
            return value[case_type]
        elif case_type == "sint64Value":
            return int(value[case_type])
        elif case_type == "fixed32Value":
            return value[case_type]
        elif case_type == "fixed64Value":
            return int(value[case_type])
        elif case_type == "sfixed32Value":
            return value[case_type]
        elif case_type == "sfixed64Value":
            return int(value[case_type])
        elif case_type == "boolValue":
            return value[case_type]
        elif case_type == "stringValue":
            return value[case_type]
        elif case_type == "bytesValue":
            return value[case_type]
        elif case_type == "structValue":
            return value[case_type]["fields"]
        elif case_type == "listValue":
            rows = []
            for v in value[case_type]["values"]:
                rows.append(parse_value(v["kind"]["$case"], v["kind"]))
            return rows

    parsed_rows = []
    for row in response.rows:
        parsed_row = {}
        for field in fields:
            value = row["value"][field]["kind"]
            case_type = value["$case"]
            parsed_row[field] = parse_value(case_type, value)
        parsed_rows.append(parsed_row)
    return pd.DataFrame.from_dict(parsed_rows)


def execute_sql(
    sql: str,
    connection_slug: str | None = None,
    database_id: str | None = None,
    base_url: str | None = None,
    team_slug: str | None = None,
    authorization: str | None = None,
    notebook_id: str | None = None,
) -> pd.DataFrame:
    config_from_env = _read_configuration_from_env()
    if database_id is None:
        database_id = config_from_env["database_id"]
    if base_url is None:
        base_url = config_from_env["base_url"]
    if team_slug is None:
        team_slug = config_from_env["team_slug"]
    if authorization is None:
        authorization = config_from_env["authorization"]
    if notebook_id is None:
        notebook_id = config_from_env["notebook_id"]

    headers = {
        "teamSlug": team_slug,
        "Authorization": authorization,
    }

    if sql.startswith("ref(") and sql.endswith(")"):
        cell_name = sql[4:-1]
        url_sql = urllib.parse.urljoin(
            _canonicalize_base_url(base_url),
            f"/canvas/{notebook_id}/cell-name/{cell_name}",
        )
        response = requests.get(url_sql, headers=headers, verify=True)
        if response.status_code != 200:
            raise MorphApiError(response.text)
        response_body = response.json()
        if response_body["cellType"] != "sql":
            raise MorphApiError(f"Cell {cell_name} is not a SQL cell")
        sql = response_body["code"]
        if response_body["connectionType"] == "external":
            connection_slug = response_body["connectionSlug"]

    url_sql = urllib.parse.urljoin(
        _canonicalize_base_url(base_url),
        f"/{database_id}/sql/python",
    )

    request = {
        "sql": sql
    }
    if connection_slug is not None:
        request["connectionSlug"] = connection_slug

    response = requests.post(url_sql, headers=headers, json=request, verify=True)
    if response.status_code != 200:
        raise MorphApiError(response.text)

    try:
        response_body = response.json()
        structured_response_body = SqlResultResponse(
            headers=response_body["headers"], rows=response_body["rows"]
        )
        df = _convert_sql_engine_response(structured_response_body)
        return df
    except Exception as e:
        raise MorphApiError(f"{e}")
