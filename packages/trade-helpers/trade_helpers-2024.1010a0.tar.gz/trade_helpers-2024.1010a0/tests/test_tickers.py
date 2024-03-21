from datetime import datetime

from src.trade_helper_0xhexe.tickers.strategy_ticker import StrategyTicker
from src.trade_helper_0xhexe.type.tick_data import TickData


def test_tickers():
    ticker = StrategyTicker()

    tick = TickData(low=100, high=200, _open=150, close=180, time=1710474320, volume=1)
    ticker.tick(tick)

    expect_1 = {
        'high': 200,
        'low': 100,
        'close': 180,
        'open': 150,
        'volume': 1,
        'color': 'green',
        'time': datetime(2024, 3, 15, 9, 15, 20)
    }

    assert ticker.processed == [
        expect_1
    ]

    tick = TickData(low=90, high=220, _open=150, close=190, time=1710474321, volume=1)
    ticker.tick(tick)

    expect_2 = {
        'high': 220,
        'low': 90,
        'close': 190,
        'open': 150,
        'volume': 2,
        'color': 'green',
        'time': datetime(2024, 3, 15, 9, 15, 20),
        'lower_band': None,
        'upper_band': None,

        'ha_close': None,
        'ha_high': None,
        'ha_low': None,
        'ha_open': None,

        'ha_upper_band': None,
        'ha_lower_band': None,
    }

    assert ticker.processed == [expect_2]

    tick = TickData(low=90, high=220, _open=150, close=190, time=1710474421, volume=1)
    ticker.tick(tick)

    expect_3 = {
         'close': 190,
         'color': 'green',
         'ha_close': 162.5,
         'ha_high': 220,
         'ha_low': 90,
         'ha_lower_band': None,
         'ha_open': 170.0,
         'ha_upper_band': None,
         'high': 220,
         'low': 90,
         'lower_band': None,
         'open': 150,
         'time': datetime(2024, 3, 15, 9, 17, 1),
         'upper_band': None,
         'volume': 1,
     }

    assert ticker.processed == [expect_2, expect_3]
