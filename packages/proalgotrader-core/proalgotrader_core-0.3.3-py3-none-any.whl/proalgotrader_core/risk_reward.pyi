from proalgotrader_core.broker_symbol import BrokerSymbol as BrokerSymbol
from proalgotrader_core.protocols.enums.position_type import PositionType as PositionType
from proalgotrader_core.protocols.enums.segment_type import SegmentType as SegmentType

TYPE_CHECKING: bool
__test__: dict

class RiskReward:
    def __init__(self, *args, **kwargs) -> None: ...
    def next(self, *args, **kwargs): ...
    @property
    def ltp(self): ...
    @property
    def trailed_stoploss(self): ...
