from functools import wraps  # for decorator
from flask import session, redirect, request, url_for, abort


# decorator to check if user is logged in
def login_required(f):
    @wraps(f)
    def decorator_function(*args, **kwargs):
        if session.get("username") is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return decorator_function


def author_required(f):
    @wraps(f)
    def decorator_function(*args, **kwargs):
        print(session.get("is_author"))
        if session.get("is_author") is None:
            abort(403)  # such error, because only shady users would do that
        return f(*args, **kwargs)

    return decorator_function

