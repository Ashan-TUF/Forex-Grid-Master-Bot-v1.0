import pandas as pd
import MetaTrader5 as mt5

class Bot:
    def __init__(self, symbol, volume, profit_target, no_of_levels, no_of_cycles, unlock_callback=None):
        self.symbol = symbol
        self.volume = volume
        self.profit_target = profit_target
        self.no_of_levels = no_of_levels
        self.no_of_cycles = no_of_cycles
        self.unlock_callback = unlock_callback

    def buy_limit(self, price, symbol, volume):
        request = {
            'action': mt5.TRADE_ACTION_PENDING,
            'symbol': symbol,
            'volume': volume,
            'type': mt5.ORDER_TYPE_BUY_LIMIT,
            'price': price,
            'magic': 100,
            'deviation': 20,
            'comment': 'python script open',
            'type_time': mt5.ORDER_TIME_GTC,
            'type_filling': mt5.ORDER_FILLING_RETURN,
        }

        result = mt5.order_send(request)
        print(result)

    def sell_limit(self, price, symbol, volume):
        request = {
            'action': mt5.TRADE_ACTION_PENDING,
            'symbol': symbol,
            'volume': volume,
            'type': mt5.ORDER_TYPE_SELL_LIMIT,
            'price': price,
            'magic': 100,
            'deviation': 20,
            'comment': 'python script open',
            'type_time': mt5.ORDER_TIME_GTC,
            'type_filling': mt5.ORDER_FILLING_RETURN,
        }

        result = mt5.order_send(request)
        print(result)

    def cal_buy_profit(self, symbol):
        data = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(data), columns=data[0]._asdict().keys())
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)

        df = df[df.type == 0]

        profit = float(df.profit.sum())
        return profit

    def cal_buy_volume(self, symbol):
        data = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(data), columns=data[0]._asdict().keys())
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)

        df = df[df.type == 0]

        volume = float(df.volume.sum())
        return volume

    def cal_sell_profit(self, symbol):
        data = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(data), columns=data[0]._asdict().keys())
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)

        df = df[df.type == 1]

        profit = float(df.profit.sum())
        return profit

    def cal_sell_volume(self, symbol):
        data = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(data), columns=data[0]._asdict().keys())
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)

        df = df[df.type == 1]

        volume = float(df.volume.sum())
        return volume

    def cal_buy_margin(self, symbol):
        data = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(data), columns=data[0]._asdict().keys())
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)

        df = df[df.type == 0]

        sum = 0

        for i in df.index:
            volume = df.volume[i]
            open_price = df.price_open[i]
            margin = mt5.order_calc_margin(mt5.ORDER_TYPE_BUY, symbol, volume, open_price)
            sum += margin

        return sum

    def cal_sell_margin(self, symbol):
        data = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(data), columns=data[0]._asdict().keys())
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)

        df = df[df.type == 1]

        sum = 0

        for i in df.index:
            volume = df.volume[i]
            open_price = df.price_open[i]
            margin = mt5.order_calc_margin(mt5.ORDER_TYPE_BUY, symbol, volume, open_price)
            sum += margin

        return sum

    def cal_buy_pct_profit(self, symbol):
        profit = self.cal_buy_profit(symbol)
        margin = self.cal_buy_margin(symbol)
        pct = (profit / margin) * 100
        return pct

    def cal_sell_pct_profit(self, symbol):
        profit = self.cal_sell_profit(symbol)
        margin = self.cal_sell_margin(symbol)
        pct = (profit / margin) * 100
        return pct

    def close_position(self, position):
        tick = mt5.symbol_info_tick(position.symbol)
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "position": position.ticket,
            "symbol": position.symbol,
            "volume": position.volume,
            "type": mt5.ORDER_TYPE_BUY if position.type == 1 else
            mt5.ORDER_TYPE_SELL,
            "price": tick.ask if position.type == 1 else tick.bid,
            "deviation": 20,
            "magic": 100,
            "comment": "python script close",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_FOK,
        }
        result = mt5.order_send(request)
        print(result)
        return result

    def close_all_positions(self, symbol):
        positions = mt5.positions_get(symbol=symbol)
        for i in positions:
            self.close_position(i)

    def delete_pending(self, ticket):
        close_request = {
            "action": mt5.TRADE_ACTION_REMOVE,
            "order": ticket,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        result = mt5.order_send(close_request)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            result_dict = result._asdict()
            print(result_dict)
        else:
            print('Delete complete...')

    def close_all_pending(self, symbol):
        orders = mt5.orders_get(symbol=symbol)
        df = pd.DataFrame(list(orders), columns=orders[0]._asdict().keys())
        df.drop(['time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial',
                 'price_stoplimit'], axis=1, inplace=True)
        df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
        for ticket in df.ticket:
            self.delete_pending(ticket)

    def draw_grid(self, symbol, volume, no_of_levels):
        pct_change_sell = 1
        tick = mt5.symbol_info_tick(symbol)
        current_price = tick.bid

        for i in range(no_of_levels):
            price = ((pct_change_sell / (100 * 100)) * current_price) + current_price
            self.sell_limit(price, symbol, volume)
            pct_change_sell += 1

        pct_change_buy = -1
        tick = mt5.symbol_info_tick(symbol)
        current_price = tick.bid

        for i in range(no_of_levels):
            price = ((pct_change_buy / (100 * 100)) * current_price) + current_price
            self.buy_limit(price, symbol, volume)
            pct_change_buy -= 1

    def run (self):
        for i in range(self.no_of_cycles):
            self.draw_grid(self.symbol, self.volume, self.no_of_levels)

            while True:
                try:
                    positions = mt5.positions_get(symbol=self.symbol)
                    if len(positions) > 0:
                        margin_b = self.cal_buy_margin(self.symbol)
                        margin_s = self.cal_sell_margin(self.symbol)

                        if margin_b > 0:
                            pct = self.cal_buy_pct_profit(self.symbol)
                            print(pct)
                            if pct >= self.profit_target:
                                self.close_all_positions(self.symbol)

                        if margin_s > 0:
                            pct = self.cal_sell_pct_profit(self.symbol)
                            print(pct)
                            if pct >= self.profit_target:
                                self.close_all_positions(self.symbol)

                        positions = mt5.positions_get(symbol=self.symbol)
                        if len(positions) == 0:
                            self.close_all_pending(self.symbol)
                            break
                except:
                    pass

        self.unlock_callback()