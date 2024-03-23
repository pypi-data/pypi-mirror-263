from __future__ import annotations

import sys
from functools import wraps
from logging import Logger as _Logger
from logging import root
from typing import Any, Callable, Type

from better_exceptions import CAP_CHAR, PIPE_CHAR, THEME, ExceptionFormatter

from cacheline.typed import T

_parent = _Logger
if root.manager.loggerClass is not None:  # pylint:disable=no-member
    _parent: Type[_Logger] = root.manager.loggerClass  # pylint:disable=no-member


class Logger(_parent):
    def __init__(self, name: str, level: int | str = 0) -> None:
        super().__init__(name, level)
        self._extra: dict[str, Any] = {}

    def set_default_extra(self, extra: dict[str, Any]) -> None:
        """
        set default extra which will add to every log
        """
        self._extra = extra

    def catch(self, func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            try:
                return func(*args, **kwargs)
            except Exception as error:
                formatter = ExceptionFormatter(
                    colored=False,
                    theme=THEME,
                    max_length=2048,
                    pipe_char=PIPE_CHAR,
                    cap_char=CAP_CHAR,
                )
                self.error(
                    "".join(
                        formatter.format_exception(
                            error.__class__, error, sys.exc_info()[2]
                        )
                    ),
                    extra=self._extra,
                )
                raise error

        return wrapper

    def _log(self, level, msg, args, **kwargs):  # type:ignore # pylint:disable=arguments-differ
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


root.manager.setLoggerClass(Logger)  # pylint:disable=no-member
