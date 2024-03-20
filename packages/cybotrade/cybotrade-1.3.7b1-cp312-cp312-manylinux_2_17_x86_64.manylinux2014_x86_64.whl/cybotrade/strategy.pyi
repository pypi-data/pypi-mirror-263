from typing import List, Dict
from .models import (
    ActiveOrder,
    OpenedTrade,
    OrderUpdate,
    Symbol
)
from .runtime import StrategyTrader

import logging

class Strategy:
    """
    This class is a handler that will be used by the Runtime to handle events such as
    `on_candle_closed`, `on_order_update`, etc. The is a base class and every new strategy
    should be inheriting this class and override the methods.
    """

    logger = logging
    LOG_FORMAT: str
    data_map: Dict[str, Dict[str,str]]

    def __init__(
            self,
            log_level: int = logging.INFO,
            handlers: List[logging.Handler] = [],
    ):
        """
        Set up the logger
        """

    def on_init(
            self,
            strategy,
    ):
        """
        This method is called when the strategy is started successfully.
        """
    
    async def set_param(
            self,
            identifier,
            value 
    ):
        """
        Set up parameter for permutation
        """


    async def on_order_update(
            self,
            strategy,
            update
    ):
        """
        This method is called when receiving an order update from the exchange.
        """

    async def on_backtest_complete(
            self, strategy
    ):
        """
        This method is called when backtest is completed.
        """

    async def on_datasource_interval(
            self, strategy, topic,
    ):
        """
        This method is called when the requested Datasources' Interval has elapsed.
        E.g 'coinglass|4h|funding' -> this gets called every 4h
        """

    async def on_trade(
            self, strategy, trade
    ):
        """
        This method is called when a trade is opened.
        """

    async def on_active_order_interval(
            self, strategy, active_orders
    ):
        """
        This method is called when the passed in `active_order_interval` time has elapsed. This will return a list of client_order_ids of all active orders.
        """

    async def on_candle_closed(
            self, strategy, topic, symbol,
    ):
        """
        This method is called when the requested candles have closed.
        """
    
    async def initialize_ringbuffer(
            self, topics, data
    ):
        """
        ***This method should never be overidden as it is used internally by the runtime.***
        """

    async def update_ringbuffer(
            self, topic, data
    ):
        """
        ***This method should never be overidden as it is used internally by the runtime.***
        """

    def get_data_map(self):
        """
        ***This method is to get the data_map from python base strategy class***
        """
