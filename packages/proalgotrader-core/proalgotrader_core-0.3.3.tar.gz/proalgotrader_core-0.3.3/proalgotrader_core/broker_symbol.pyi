from proalgotrader_core.base_symbol import BaseSymbol as BaseSymbol
from proalgotrader_core.protocols.enums.segment_type import SegmentType as SegmentType
from proalgotrader_core.tick import Tick as Tick

TYPE_CHECKING: bool
__test__: dict

class BrokerSymbol:
    def __init__(self, *args, **kwargs) -> None: ...
    def on_tick(self, *args, **kwargs): ...
    @property
    def can_trade(self): ...
