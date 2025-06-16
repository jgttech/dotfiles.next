from click import make_pass_decorator
from .Context import Context

pass_context = make_pass_decorator(Context, ensure=True)
