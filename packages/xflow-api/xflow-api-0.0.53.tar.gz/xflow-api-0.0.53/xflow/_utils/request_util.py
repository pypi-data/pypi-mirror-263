import os
from typing import Any

import requests


def post(url: str, data: dict, options: dict | None = None, target_system_name: str | None = None) -> tuple[int, Any]:
    args = {"url": url, "json": data}
    if "VERIFY_SSL" in os.environ:
        if not bool(int(os.environ["VERIFY_SSL"])):
            args["verify"] = False
    try:
        response = requests.post(**args)
    except requests.exceptions.ConnectionError:
        msg = "connection error"
        if target_system_name is not None:
            msg = msg + f": can't make connection with {target_system_name}"
        return -1, msg
    else:
        if response.status_code == 200:
            if response.json()["CODE"] != "00":
                return -1, response.json()["ERROR_MSG"]
        else:
            msg = f"server error. status code: {str(response.status_code)}"
            if target_system_name is not None:
                msg = f"internal server error on {target_system_name}. status code: {str(response.status_code)}"
            return -1, msg
    return 0, response.json()


def get(url: str, options: dict | None = None, target_system_name: str | None = None) -> tuple[int, Any]:
    args = {"url": url}
    if "VERIFY_SSL" in os.environ:
        if not bool(int(os.environ["VERIFY_SSL"])):
            args["verify"] = False
    try:
        response = requests.get(**args)
    except requests.exceptions.ConnectionError:
        msg = "connection error"
        if target_system_name is not None:
            msg = msg + f": can't make connection with {target_system_name}"
        return -1, msg
    else:
        if response.status_code == 200:
            if response.json()["CODE"] != "00":
                return -1, response.json()["ERROR_MSG"]
        else:
            msg = f"server error. status code: {str(response.status_code)}"
            if target_system_name is not None:
                msg = f"internal server error on {target_system_name}. status code: {str(response.status_code)}"
            return -1, msg
    return 0, response.json()
