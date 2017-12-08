from functools import wraps # for decorator
from flask import session, redirect, request, url_for


# decorator to check if user is logged in
def login_required(f):
    @wraps(f)
    def decorator_function(*args, **kwargs):
        if session.get("username") is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorator_function
