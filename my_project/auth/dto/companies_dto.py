from flask import abort
from my_project.auth.dto._common import (
    require_dict, reject_unknown, require_keys, as_str, as_email, as_pos_int,
)

FIELDS = ("company_name", "contact_email", "developer_id")


def parse_create(data):
    data = require_dict(data)
    reject_unknown(data, FIELDS)
    require_keys(data, ("company_name", "developer_id"))
    return {
        "company_name": as_str(data, "company_name", 60),
        "contact_email": as_email(data, "contact_email", required=False, allow_null=True)
        if "contact_email" in data else None,
        "developer_id": as_pos_int(data, "developer_id"),
    }


def parse_put(data):
    data = require_dict(data)
    reject_unknown(data, FIELDS)
    require_keys(data, FIELDS)
    return {
        "company_name": as_str(data, "company_name", 60),
        "contact_email": as_email(data, "contact_email", allow_null=True),
        "developer_id": as_pos_int(data, "developer_id"),
    }


def parse_patch(data):
    data = require_dict(data)
    if len(data) == 0:
        abort(400, description="Empty body")
    reject_unknown(data, FIELDS)
    out = {}
    if "company_name" in data:
        out["company_name"] = as_str(data, "company_name", 60)
    if "contact_email" in data:
        out["contact_email"] = as_email(data, "contact_email", allow_null=True)
    if "developer_id" in data:
        out["developer_id"] = as_pos_int(data, "developer_id")
    return out
