from __future__ import annotations

from threading import local

from typing import Any, Callable, Generator, Self, overload

__all__ = ["context_mgr"]


type GenType[YieldT] = Generator[YieldT, BaseException | None, Any]


class _LocalCtx(local):
    def __init__(self):
        self.stack: list[ContextMgr] = []


ctx = _LocalCtx()


class ContextMgrFactory[**ArgT, YieldT]:
    def __init__(self, genfunc: Callable[ArgT, GenType[YieldT]]):
        self.genfunc = genfunc

    def __call__(self, *args: ArgT.args, **kwargs: ArgT.kwargs) -> ContextMgr[YieldT]:
        """Call the wrapped Generator function"""
        return ContextMgr(self.genfunc(*args, **kwargs))


class ContextMgrAutoCallable[**P, YieldT](ContextMgrFactory[[], YieldT]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __enter__(self) -> YieldT:
        mgr = self()

        ctx.stack.append(mgr)

        return mgr.__enter__()

    def __exit__(self, exc_tp, exc, exc_tb) -> bool:
        mgr = ctx.stack.pop()

        return mgr.__exit__(exc_tp, exc, exc_tb)

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> ContextMgr[YieldT]:
        return super().__call__(*args, **kwargs)


class ContextMgr[YieldT]:
    def __init__(self, gen: GenType[YieldT]):
        self.gen = gen

    def __enter__(self) -> YieldT:
        return next(self.gen)

    def __exit__(self, exc_type, exc: BaseException | None, exc_tb) -> bool:
        try:
            self.gen.send(exc)
        except StopIteration as e:
            return bool(e.value)

        raise TypeError("Generator should only yield once.")


@overload
def context_mgr[
    **P, YieldT
](func: Callable[[], GenType[YieldT]]) -> ContextMgrAutoCallable[P, YieldT]: ...


@overload
def context_mgr[
    **P, YieldT
](func: Callable[P, GenType[YieldT]]) -> ContextMgrFactory[P, YieldT]: ...


def context_mgr(func):  # type: ignore
    return ContextMgrAutoCallable(func)
