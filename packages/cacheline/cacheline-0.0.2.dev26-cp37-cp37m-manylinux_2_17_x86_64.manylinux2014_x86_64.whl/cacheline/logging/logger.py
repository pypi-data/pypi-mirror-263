from __future__ import annotations

import functools
import inspect
from logging import Logger as _Logger
from logging import root
from traceback import format_exception
from typing import Any, Callable, Type

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
        this = self

        class Catcher:
            def __enter__(self):
                return None

            def __exit__(self, _type, value, _traceback):
                if _type is None:
                    return None
                if not issubclass(_type, Exception):
                    return False
                formatted = "".join(format_exception(_type, value, _traceback))
                this.error(formatted, extra=this._extra)
                return False

            def __call__(self) -> Any:
                catcher = Catcher()
                if inspect.iscoroutinefunction(func):

                    async def wrapper(*args, **kwargs) -> T:
                        with catcher:
                            return await func(*args, **kwargs)
                elif inspect.isgeneratorfunction(func):

                    def wrapper(*args, **kwargs) -> T:
                        with catcher:
                            return (yield from func(*args, **kwargs))
                else:

                    def wrapper(*args, **kwargs) -> T:
                        with catcher:
                            return func(*args, **kwargs)

                functools.update_wrapper(wrapper, func)
                return wrapper

        return Catcher()()

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
