import re
from datetime import datetime
from flask import abort

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def require_dict(data):
    if data is None or not isinstance(data, dict):
        abort(400, description="No input data provided")
    return data


def reject_unknown(data, allowed):
    unknown = sorted(k for k in data if k not in allowed)
    if unknown:
        abort(400, description="Unknown fields: " + ", ".join(unknown))


def require_keys(data, keys):
    missing = sorted(k for k in keys if k not in data)
    if missing:
        abort(400, description="Missing required fields: " + ", ".join(missing))


def require_non_null(data, keys):
    for k in keys:
        if data.get(k) is None:
            abort(400, description=f"Field '{k}' cannot be null")


def as_str(data, key, max_len, required=True, allow_null=False):
    if key not in data:
        if required:
            abort(400, description=f"Missing required field: {key}")
        return None
    val = data[key]
    if val is None:
        if allow_null:
            return None
        abort(400, description=f"Field '{key}' cannot be null")
    if not isinstance(val, str):
        abort(400, description=f"Field '{key}' must be a string")
    if not allow_null and len(val.strip()) == 0:
        abort(400, description=f"Field '{key}' cannot be empty")
    if len(val) > max_len:
        abort(400, description=f"Field '{key}' exceeds max length {max_len}")
    return val


def as_email(data, key, max_len=255, required=True, allow_null=False):
    val = as_str(data, key, max_len, required=required, allow_null=allow_null)
    if val is None:
        return None
    if not EMAIL_RE.match(val):
        abort(400, description=f"Field '{key}' must be a valid email")
    return val


def as_pos_int(data, key, required=True, allow_null=False):
    if key not in data:
        if required:
            abort(400, description=f"Missing required field: {key}")
        return None
    val = data[key]
    if val is None:
        if allow_null:
            return None
        abort(400, description=f"Field '{key}' cannot be null")
    if isinstance(val, bool) or not isinstance(val, int):
        abort(400, description=f"Field '{key}' must be a positive integer")
    if val <= 0:
        abort(400, description=f"Field '{key}' must be a positive integer")
    return val


def as_datetime(data, key, required=True, allow_null=False):
    if key not in data:
        if required:
            abort(400, description=f"Missing required field: {key}")
        return None
    val = data[key]
    if val is None:
        if allow_null:
            return None
        abort(400, description=f"Field '{key}' cannot be null")
    if not isinstance(val, str):
        abort(400, description=f"Field '{key}' must be an ISO 8601 datetime string")
    try:
        return datetime.fromisoformat(val.replace("Z", "+00:00")).replace(tzinfo=None)
    except ValueError:
        abort(400, description=f"Field '{key}' must be an ISO 8601 datetime string")


def as_rating(data, key, required=True, allow_null=False):
    if key not in data:
        if required:
            abort(400, description=f"Missing required field: {key}")
        return None
    val = data[key]
    if val is None:
        if allow_null:
            return None
        abort(400, description=f"Field '{key}' cannot be null")
    if isinstance(val, bool) or not isinstance(val, (int, float)):
        abort(400, description=f"Field '{key}' must be a number")
    fval = float(val)
    if fval < 0.0 or fval > 5.0:
        abort(400, description="rating must be between 0.0 and 5.0")
    # at most one decimal digit
    if round(fval, 1) != fval:
        abort(400, description="rating must have at most one decimal digit")
    return round(fval, 1)


def as_size_bytes(data, key, required=True):
    if key not in data:
        if required:
            abort(400, description=f"Missing required field: {key}")
        return None
    val = data[key]
    if val is None:
        abort(400, description=f"Field '{key}' cannot be null")
    if isinstance(val, bool) or not isinstance(val, int):
        abort(400, description=f"Field '{key}' must be a positive integer")
    if val <= 0 or val > 18446744073709551615:
        abort(400, description=f"Field '{key}' out of BIGINT UNSIGNED range")
    return val


def as_status(data, key, required=True, allow_null=False):
    if key not in data:
        if required:
            abort(400, description=f"Missing required field: {key}")
        return None
    val = data[key]
    if val is None:
        if allow_null:
            return None
        abort(400, description=f"Field '{key}' cannot be null")
    if val not in ("published", "unpublished", "suspended"):
        abort(400, description="status must be published, unpublished, or suspended")
    return val


def as_password(data, key="password", required=True):
    val = as_str(data, key, 128, required=required, allow_null=False)
    if val is None:
        return None
    if len(val) < 8:
        abort(400, description="password must be at least 8 characters")
    return val
