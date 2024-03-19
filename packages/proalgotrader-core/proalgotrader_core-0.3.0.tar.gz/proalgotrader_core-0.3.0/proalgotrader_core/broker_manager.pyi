from proalgotrader_core.algo_session import AlgoSession as AlgoSession
from proalgotrader_core.api import Api as Api
from proalgotrader_core.brokers.base_broker import BaseBroker as BaseBroker

__test__: dict
providers: dict

class BrokerManager:
    def get_instance(self, *args, **kwargs): ...
