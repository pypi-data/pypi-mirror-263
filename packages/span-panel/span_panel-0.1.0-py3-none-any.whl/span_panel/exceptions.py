from __future__ import annotations


class SpanError(Exception):
    pass


class NotAuthorizedError(SpanError):
    pass


class BadRequestError(SpanError):
    pass
