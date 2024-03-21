from typing import List, Dict

import numpy as np

from src.trade_helper_0xhexe.type.tick_data import TickData


class StrategyTicker:
    def __init__(self, _timedelta=60, start_hour=9, start_minute=15, start_second=0,
                 processed: List[Dict] = None, period=20, num_std=2):
        if processed is None:
            processed = []

        self._timedelta = _timedelta
        self.processed = processed

        self.start_hour = start_hour
        self.start_minute = start_minute
        self.start_second = start_second

        self.period = period
        self.num_std = num_std

    def tick(self, tick: TickData):
        if len(self.processed) == 0:
            self.processed.append(tick.to_dict())
            return

        last_item = self.processed[-1]

        if (tick.time - last_item["time"]).total_seconds() >= self._timedelta:
            tick_dict = tick.to_dict()
            self.processed.append(tick_dict)
            last_item = self.processed[-1]
        else:
            last_item["low"] = min(last_item["low"], tick.low)
            last_item["high"] = max(last_item["high"], tick.high)
            last_item["close"] = tick.close
            last_item["volume"] += tick.volume

        ha_open, ha_close, ha_high, ha_low, ha_color = self.calculate_heiken_ashi()

        last_item["ha_open"] = ha_open
        last_item["ha_close"] = ha_close
        last_item["ha_high"] = ha_high
        last_item["ha_low"] = ha_low
        last_item["ha_color"] = ha_color
        last_item["color"] = "green" if last_item["open"] < last_item["close"] else "red"

        ha_bb, normal_bb = self.calculate_bb()

        if ha_bb is not None and normal_bb is not None:
            last_item["ha_lower_band"], last_item["ha_upper_band"] = ha_bb
            last_item["lower_band"], last_item["upper_band"] = normal_bb

    def process(self):
        pass

    def __getitem__(self, index):
        if index >= 0:
            if index < len(self.processed):
                return self.processed[len(self.processed) - 1 - index]
            else:
                raise IndexError("Index out of range")
        else:
            return self.processed[index]

    def calculate_bb(self):
        def calculate_bb(key: str = 'ha_close'):
            if len(self.processed) < self.period:
                return None, None

            data_list = [data if key in data else data['close'] for data in self.processed[-self.period:]]
            closes = np.array(data_list)
            sma = np.mean(closes)
            std_dev = np.std(closes)

            upper_band = sma + (self.num_std * std_dev)
            lower_band = sma - (self.num_std * std_dev)

            return lower_band, upper_band

        return calculate_bb('ha_close'), calculate_bb('close')

    def calculate_heiken_ashi(self):
        if len(self.processed) < 2:
            return None, None, None, None

        current_item = self.processed[-1]
        previous_item = self.processed[-2]

        prev_open_ha = previous_item.get("ha_open", previous_item["open"])
        if prev_open_ha is None:
            prev_open_ha = previous_item["open"]

        prev_close_ha = previous_item.get("ha_close", previous_item["close"])
        if prev_close_ha is None:
            prev_close_ha = previous_item['close']

        ha_close = (current_item["open"] + current_item["high"] + current_item["low"] + current_item["close"]) / 4
        ha_open = (prev_open_ha + prev_close_ha) / 2
        ha_high = max(current_item["high"], ha_open, ha_close)
        ha_low = min(current_item["low"], ha_open, ha_close)

        ha_color = "green" if ha_open < ha_close else "red"

        return ha_open, ha_close, ha_high, ha_low, ha_color
