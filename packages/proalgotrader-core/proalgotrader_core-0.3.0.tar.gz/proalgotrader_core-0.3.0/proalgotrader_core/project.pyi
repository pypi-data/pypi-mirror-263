from proalgotrader_core.api import Api as Api
from proalgotrader_core.broker import Broker as Broker
from proalgotrader_core.data_broker import DataBroker as DataBroker
from proalgotrader_core.github_repository import GithubRepository as GithubRepository

__test__: dict

class Project:
    def __init__(self, *args, **kwargs) -> None: ...
    def clone_repository(self, *args, **kwargs): ...
