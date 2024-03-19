import proalgotrader_core.token_managers.base_token_manager
from proalgotrader_core.helpers.get_totp import get_totp as get_totp
from proalgotrader_core.token_managers.base_token_manager import BaseTokenManager as BaseTokenManager

__test__: dict

class ShoonyaTokenManager(proalgotrader_core.token_managers.base_token_manager.BaseTokenManager):
    def __init__(self, *args, **kwargs) -> None: ...
    def get_token(self, *args, **kwargs): ...
    def set_token(self, *args, **kwargs): ...
