from flask import abort

RESOURCE_FIELDS = {
    'accounts': {
        'writable': ('email', 'password_hash', 'name', 'is_developer', 'country'),
        'nullable': (),
        'read_only': ('id', 'created_at'),
    },
    'devices': {
        'writable': ('model', 'os_version'),
        'nullable': (),
        'read_only': ('id',),
    },
    'accounts_devices': {
        'writable': (),
        'nullable': (),
        'read_only': ('account_id', 'device_id'),
    },
    'companies': {
        'writable': ('company_name', 'contact_email', 'developer_account_id'),
        'nullable': ('contact_email',),
        'read_only': ('id',),
    },
    'apps': {
        'writable': ('title', 'caption', 'price', 'currency', 'company_id'),
        'nullable': ('caption',),
        'read_only': ('id',),
    },
    'installations': {
        'writable': ('installed_at',),
        'nullable': (),
        'read_only': ('app_id', 'device_id'),
    },
    'apps_versions': {
        'writable': ('app_id', 'version', 'size_bytes'),
        'nullable': (),
        'read_only': ('id', 'created_at'),
    },
    'apps_discounts': {
        'writable': ('app_id', 'discount_price', 'starts_at', 'ends_at'),
        'nullable': (),
        'read_only': ('id',),
    },
    'categories': {
        'writable': ('name',),
        'nullable': (),
        'read_only': ('id',),
    },
    'apps_categories': {
        'writable': (),
        'nullable': (),
        'read_only': ('app_id', 'category_id'),
    },
    'reviews': {
        'writable': ('rating', 'comment'),
        'nullable': ('comment',),
        'read_only': ('account_id', 'app_id', 'created_at'),
    },
    'payment_cards': {
        'writable': ('account_id', 'token', 'card_brand', 'exp_date', 'last4'),
        'nullable': (),
        'read_only': ('id',),
    },
    'bills': {
        'writable': ('currency', 'amount_paid', 'payment_card_id', 'paid_at', 'discount_id'),
        'nullable': ('discount_id',),
        'read_only': ('account_id', 'app_id'),
    },
    'library': {
        'writable': ('app_data', 'last_opened_at'),
        'nullable': ('app_data', 'last_opened_at'),
        'read_only': ('app_id', 'account_id'),
    },
}

def prepare_update(resource_name, data, partial=False):
    if data is None or not isinstance(data, dict):
        abort(400, description="No input data provided")

    spec = RESOURCE_FIELDS[resource_name]
    writable = set(spec['writable'])
    nullable = set(spec['nullable'])
    read_only = set(spec['read_only'])

    if partial and len(data) == 0:
        abort(400, description="Empty body")

    unknown = sorted(k for k in data if k not in writable and k not in read_only)
    if unknown:
        abort(400, description="Unknown fields: " + ", ".join(unknown))

    readonly_attempts = sorted(k for k in data if k in read_only)
    if readonly_attempts:
        abort(400, description="Read-only fields cannot be changed: " + ", ".join(readonly_attempts))

    if not partial:
        missing = sorted(f for f in writable if f not in data)
        if missing:
            abort(400, description="Missing required fields: " + ", ".join(missing))
        for field in writable:
            if data[field] is None and field not in nullable:
                abort(400, description=f"Field '{field}' cannot be null")
        return {field: data[field] for field in writable}

    result = {}
    for field in data:
        if field not in writable:
            continue
        if data[field] is None and field not in nullable:
            abort(400, description=f"Field '{field}' cannot be null")
        result[field] = data[field]
    return result
