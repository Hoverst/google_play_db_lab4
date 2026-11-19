from flask import abort
from my_project.auth.dto._common import (
    require_dict, reject_unknown, require_keys, as_str, as_pos_int, as_size_bytes,
)

FIELDS = ("app_id", "version", "size_bytes")


def parse_create(data):
    data = require_dict(data)
    reject_unknown(data, FIELDS)
    require_keys(data, FIELDS)
    return {
        "app_id": as_pos_int(data, "app_id"),
        "version": as_str(data, "version", 20),
        "size_bytes": as_size_bytes(data, "size_bytes"),
    }


def parse_put(data):
    return parse_create(data)


def parse_patch(data):
    data = require_dict(data)
    if len(data) == 0:
        abort(400, description="Empty body")
    reject_unknown(data, FIELDS)
    out = {}
    if "app_id" in data:
        out["app_id"] = as_pos_int(data, "app_id")
    if "version" in data:
        out["version"] = as_str(data, "version", 20)
    if "size_bytes" in data:
        out["size_bytes"] = as_size_bytes(data, "size_bytes")
    return out
