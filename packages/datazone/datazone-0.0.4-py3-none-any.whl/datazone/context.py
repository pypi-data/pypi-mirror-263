from contextvars import ContextVar

inspect_mode = ContextVar("inspect_mode", default=False)
profile_context: ContextVar[str | None] = ContextVar("profile_context", default=None)
