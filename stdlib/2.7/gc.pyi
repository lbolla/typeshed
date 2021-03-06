"""Stubs for the 'gc' module."""

from typing import List, Any, Tuple

def enable() -> None: ...
def disable() -> None: ...
def isenabled() -> bool: ...
def collect(generation: int = ...) -> int: ...
def set_debug(flags: int) -> None: ...
def get_debug() -> int: ...
def get_objects() -> List[Any]: ...
def set_threshold(threshold0: int, threshold1: int = ..., threshold2: int = ...) -> None: ...
def get_count() -> Tuple[int, int, int]: ...
def get_threshold() -> Tuple[int, int, int]: ...
def get_referrers(*objs: Any) -> List[Any]: ...
def get_referents(*objs: Any) -> List[Any]: ...
def is_tracked(obj: Any) -> bool: ...

garbage = ... # type: List[Any]

DEBUG_STATS = ... # type: Any
DEBUG_COLLECTABLE = ... # type: Any
DEBUG_UNCOLLECTABLE = ... # type: Any
DEBUG_INSTANCES = ... # type: Any
DEBUG_OBJECTS = ... # type: Any
DEBUG_SAVEALL = ... # type: Any
DEBUG_LEAK = ... # type: Any
