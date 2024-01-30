from __future__ import annotations

from collections.abc import Callable, Coroutine
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Literal, Union

if TYPE_CHECKING:
    from crawlee.autoscaling.system_status import SystemInfo


@dataclass
class EventPersistStateData:
    """Data for the persist state event."""

    is_migrating: bool


@dataclass
class EventSystemInfoData:
    """Data for the system info event."""

    system_info: SystemInfo


@dataclass
class EventMigratingData:
    """Data for the migrating event."""


@dataclass
class EventAbortingData:
    """Data for the aborting event."""


@dataclass
class EventExitData:
    """Data for the exit event."""


Event = Literal['persist_state', 'system_info', 'migrating', 'aborting', 'exit']
EventData = Union[EventPersistStateData, EventSystemInfoData, EventMigratingData, EventAbortingData, EventExitData]
SyncListener = Callable[..., None]
AsyncListener = Callable[..., Coroutine[Any, Any, None]]
Listener = Union[SyncListener, AsyncListener]
WrappedListener = Callable[..., Coroutine[Any, Any, None]]
