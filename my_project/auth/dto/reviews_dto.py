from flask import abort
from my_project.auth.dto._common import (
    require_dict, reject_unknown, require_keys, as_pos_int, as_str, as_rating,
)

CREATE_FIELDS = ("account_id", "app_id", "rating", "comment")
UPDATE_FIELDS = ("rating", "comment")


def parse_create(data):
    data = require_dict(data)
    reject_unknown(data, CREATE_FIELDS)
    require_keys(data, ("account_id", "app_id", "rating"))
    out = {
        "account_id": as_pos_int(data, "account_id"),
        "app_id": as_pos_int(data, "app_id"),
        "rating": as_rating(data, "rating"),
    }
    if "comment" in data:
        out["comment"] = as_str(data, "comment", 350, allow_null=True)
    else:
        out["comment"] = None
    return out


def parse_put(data):
    data = require_dict(data)
    reject_unknown(data, UPDATE_FIELDS)
    require_keys(data, UPDATE_FIELDS)
    return {
        "rating": as_rating(data, "rating"),
        "comment": as_str(data, "comment", 350, allow_null=True),
    }


def parse_patch(data):
    data = require_dict(data)
    if len(data) == 0:
        abort(400, description="Empty body")
    reject_unknown(data, UPDATE_FIELDS)
    out = {}
    if "rating" in data:
        out["rating"] = as_rating(data, "rating")
    if "comment" in data:
        out["comment"] = as_str(data, "comment", 350, allow_null=True)
    return out
