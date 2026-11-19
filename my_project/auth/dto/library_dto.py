from flask import abort
from my_project.auth.dto._common import (
    require_dict, reject_unknown, require_keys, as_pos_int, as_str, as_datetime,
)

CREATE_FIELDS = ("account_id", "app_id", "last_opened_at", "data_ref")
PUT_FIELDS = ("account_id", "app_id", "last_opened_at", "data_ref")
PATCH_FIELDS = ("account_id", "app_id", "last_opened_at", "data_ref")


def parse_create(data):
    data = require_dict(data)
    reject_unknown(data, CREATE_FIELDS)
    require_keys(data, ("account_id", "app_id"))
    out = {
        "account_id": as_pos_int(data, "account_id"),
        "app_id": as_pos_int(data, "app_id"),
    }
    if "last_opened_at" in data:
        out["last_opened_at"] = as_datetime(data, "last_opened_at", allow_null=True)
    if "data_ref" in data:
        out["data_ref"] = as_str(data, "data_ref", 255, allow_null=True)
    return out


def parse_put(data):
    data = require_dict(data)
    reject_unknown(data, PUT_FIELDS)
    require_keys(data, PUT_FIELDS)
    return {
        "account_id": as_pos_int(data, "account_id"),
        "app_id": as_pos_int(data, "app_id"),
        "last_opened_at": as_datetime(data, "last_opened_at", allow_null=True),
        "data_ref": as_str(data, "data_ref", 255, allow_null=True),
    }


def parse_patch(data):
    data = require_dict(data)
    if len(data) == 0:
        abort(400, description="Empty body")
    reject_unknown(data, PATCH_FIELDS)
    out = {}
    if "account_id" in data:
        out["account_id"] = as_pos_int(data, "account_id")
    if "app_id" in data:
        out["app_id"] = as_pos_int(data, "app_id")
    if "last_opened_at" in data:
        out["last_opened_at"] = as_datetime(data, "last_opened_at", allow_null=True)
    if "data_ref" in data:
        out["data_ref"] = as_str(data, "data_ref", 255, allow_null=True)
    return out
