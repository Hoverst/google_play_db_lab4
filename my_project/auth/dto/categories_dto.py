from flask import abort
from my_project.auth.dto._common import require_dict, reject_unknown, require_keys, as_str

FIELDS = ("name",)


def parse_create(data):
    data = require_dict(data)
    reject_unknown(data, FIELDS)
    require_keys(data, FIELDS)
    return {"name": as_str(data, "name", 45)}


def parse_put(data):
    return parse_create(data)


def parse_patch(data):
    data = require_dict(data)
    if len(data) == 0:
        abort(400, description="Empty body")
    reject_unknown(data, FIELDS)
    return {"name": as_str(data, "name", 45)}
