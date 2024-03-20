import proalgotrader_core.protocols.enums.symbols.index_type
import proalgotrader_core.protocols.enums.symbols.stock_type
from proalgotrader_core.protocols.enums.symbols.index_type import IndexType as IndexType
from proalgotrader_core.protocols.enums.symbols.stock_type import StockType as StockType
from typing import ClassVar

__test__: dict

class SymbolType:
    Index: ClassVar[proalgotrader_core.protocols.enums.symbols.index_type.IndexType] = ...
    NIFTY_50: ClassVar[list] = ...
    Stock: ClassVar[proalgotrader_core.protocols.enums.symbols.stock_type.StockType] = ...
