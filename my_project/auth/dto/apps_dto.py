from flask import abort
from my_project.auth.dto._common import (
    require_dict, reject_unknown, require_keys, as_str, as_pos_int, as_status,
)

FIELDS = ("title", "package_name", "caption", "company_id", "status")


def parse_create(data):
    data = require_dict(data)
    reject_unknown(data, FIELDS)
    require_keys(data, ("title", "package_name", "company_id"))
    out = {
        "title": as_str(data, "title", 80),
        "package_name": as_str(data, "package_name", 150),
        "company_id": as_pos_int(data, "company_id"),
    }
    if "caption" in data:
        out["caption"] = as_str(data, "caption", 600, allow_null=True)
    else:
        out["caption"] = None
    if "status" in data:
        out["status"] = as_status(data, "status")
    return out


def parse_put(data):
    data = require_dict(data)
    reject_unknown(data, FIELDS)
    require_keys(data, FIELDS)
    return {
        "title": as_str(data, "title", 80),
        "package_name": as_str(data, "package_name", 150),
        "caption": as_str(data, "caption", 600, allow_null=True),
        "company_id": as_pos_int(data, "company_id"),
        "status": as_status(data, "status"),
    }


def parse_patch(data):
    data = require_dict(data)
    if len(data) == 0:
        abort(400, description="Empty body")
    reject_unknown(data, FIELDS)
    out = {}
    if "title" in data:
        out["title"] = as_str(data, "title", 80)
    if "package_name" in data:
        out["package_name"] = as_str(data, "package_name", 150)
    if "caption" in data:
        out["caption"] = as_str(data, "caption", 600, allow_null=True)
    if "company_id" in data:
        out["company_id"] = as_pos_int(data, "company_id")
    if "status" in data:
        out["status"] = as_status(data, "status")
    return out


def parse_attach_category(data):
    data = require_dict(data)
    reject_unknown(data, ("category_id",))
    require_keys(data, ("category_id",))
    return as_pos_int(data, "category_id")
