from __future__ import annotations

import sys
from functools import wraps
from logging import Logger as _Logger
from logging import root
from typing import Any, Callable

from cacheline.typed import T

_parent = _Logger
if root.manager.loggerClass is not None:
    _parent = root.manager.loggerClass


class Logger(_parent):
    def __init__(self, name: str, level: int | str = 0) -> None:
        super().__init__(name, level)
        self._extra = {}

    def set_default_extra(self, extra: dict[str, Any]) -> None:
        self._extra = extra

    def catch(self, func: Callable[..., T]) -> T:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                self.exception(e, extra=self._extra)
                raise e

        return wrapper

    def _log(self, level, msg, args, **kwargs):
        kwargs["extra"] = {
            **self._extra,
            **kwargs.get("extra", {}),
        }
        super()._log(
            level,
            msg,
            args,
            **kwargs,
        )


root.manager.setLoggerClass(Logger)
