#coding: utf-8

from .position import Positions

# TODO make field readonly
# TODO use nametuple to reduce memory

class Portfolio(object):

    def __init__(self):
        self.starting_cash = 0.         # float	回测或实盘交易给算法策略设置的初始资金
        self.cash = 0.                  # float	现在投资组合中剩余的现金
        self.total_returns = 0.         # float	算法投资组合至今的累积百分比收益率。计算方法是现在的投资组合价值/投资组合的初始资金。投资组合价值包含剩余现金和其市场价值。
        self.daily_returns = 0.         # float 每日收益变化
        self.market_value = 0.          # float	投资组合当前的市场价值（未实现/平仓的价值）
        self.portfolio_value = 0.       # float	当前投资组合的总共价值，包含市场价值和剩余现金。
        self.pnl = 0.                   # float	当前投资组合的￥盈亏
        self.annualized_returns = 0.    # float	投资组合的年化收益率
        self.positions = Positions()    # Dictionary	一个包含所有仓位的字典，以id_or_symbol作为键，position对象作为值，关于position的更多的信息可以在下面的部分找到。
        self.start_date = None          # DateTime	策略投资组合的回测/实时模拟交易的开始日期
        self.total_commission = 0.      # float 总的交易费
        self.total_tax = 0.

    def __repr__(self):
        return "Portfolio({0})".format({
            k: v
            for k, v in self.__dict__.items()
            if not k.startswith("_")
        })
