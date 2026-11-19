from flask import abort
from my_project.auth.dto._common import require_dict, reject_unknown, require_keys, as_pos_int

FIELDS = ("device_id", "app_version_id")


def parse_create(data):
    data = require_dict(data)
    reject_unknown(data, FIELDS)
    require_keys(data, FIELDS)
    return {
        "device_id": as_pos_int(data, "device_id"),
        "app_version_id": as_pos_int(data, "app_version_id"),
    }


def parse_put(data):
    return parse_create(data)


def parse_patch(data):
    data = require_dict(data)
    if len(data) == 0:
        abort(400, description="Empty body")
    reject_unknown(data, FIELDS)
    out = {}
    if "device_id" in data:
        out["device_id"] = as_pos_int(data, "device_id")
    if "app_version_id" in data:
        out["app_version_id"] = as_pos_int(data, "app_version_id")
    return out
