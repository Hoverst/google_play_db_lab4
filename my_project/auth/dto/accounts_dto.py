from flask import abort
from my_project.auth.dto._common import (
    require_dict, reject_unknown, require_keys, as_email, as_str, as_password, as_pos_int,
)


CREATE_FIELDS = ("email", "password", "name")
PUT_FIELDS = ("email", "password", "name")
PATCH_FIELDS = ("email", "password", "name")


def parse_create(data):
    data = require_dict(data)
    reject_unknown(data, CREATE_FIELDS)
    require_keys(data, CREATE_FIELDS)
    return {
        "email": as_email(data, "email"),
        "password": as_password(data, "password"),
        "name": as_str(data, "name", 70),
    }


def parse_put(data):
    data = require_dict(data)
    reject_unknown(data, PUT_FIELDS)
    require_keys(data, PUT_FIELDS)
    return {
        "email": as_email(data, "email"),
        "password": as_password(data, "password"),
        "name": as_str(data, "name", 70),
    }


def parse_patch(data):
    data = require_dict(data)
    if len(data) == 0:
        abort(400, description="Empty body")
    reject_unknown(data, PATCH_FIELDS)
    out = {}
    if "email" in data:
        out["email"] = as_email(data, "email")
    if "password" in data:
        out["password"] = as_password(data, "password")
    if "name" in data:
        out["name"] = as_str(data, "name", 70)
    return out


def parse_attach_device(data):
    data = require_dict(data)
    reject_unknown(data, ("device_id",))
    require_keys(data, ("device_id",))
    return as_pos_int(data, "device_id")
