from flask import request

BOOL_TRUISH = ['true', '1', 'yes', 'y', 't']


def arg_bool(name, default=False):
    """ Fetch a query argument, as a boolean. """
    v = request.args.get(name, '')
    if not len(v):
        return default
    return v in BOOL_TRUISH


def arg_int(name, default=None):
    """ Fetch a query argument, as an integer. """
    try:
        v = request.args.get(name)
        return int(v)
    except (ValueError, TypeError):
        return default


def get_limit(default=50, field='limit'):
    """ Get a limit argument. """
    return max(0, min(1000, arg_int(field, default=default)))


def get_offset(default=0, field='offset'):
    """ Get an offset argument. """
    return max(0, arg_int(field, default=default))
