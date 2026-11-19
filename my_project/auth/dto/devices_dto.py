from flask import abort
from my_project.auth.dto._common import require_dict, reject_unknown, require_keys, as_str

FIELDS = ("model", "os_version")


def parse_create(data):
    data = require_dict(data)
    reject_unknown(data, FIELDS)
    require_keys(data, FIELDS)
    return {"model": as_str(data, "model", 45), "os_version": as_str(data, "os_version", 20)}


def parse_put(data):
    return parse_create(data)


def parse_patch(data):
    data = require_dict(data)
    if len(data) == 0:
        abort(400, description="Empty body")
    reject_unknown(data, FIELDS)
    out = {}
    if "model" in data:
        out["model"] = as_str(data, "model", 45)
    if "os_version" in data:
        out["os_version"] = as_str(data, "os_version", 20)
    return out
