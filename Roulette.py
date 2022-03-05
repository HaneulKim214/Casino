"""
Roulette class script.

"""


import numpy as np
import pandas as pd

from util import append_side_bets, add_2to1, calc_bets, create_wheel


class Roulette:
    def  __init__(self, min_bet, max_bet, type):
        # self.players = {}
        self.numbers = list(range(0, 37))
        self.wheel = create_wheel(type)
        self.roll_history = []
        self.bet_history = []
        self.color_history = []
        self.type = type
        self.min_bet = min_bet
        self.max_bet = max_bet
        if type == "us":
            self.numbers.append(0)

    def roll(self, bets):
        k = np.random.choice(self.numbers)
        self.roll_history.append(k)
        self.bet_history.append(bets)

        # all bets that won.
        winning_bets = self.wheel[k] + [k]
        color = winning_bets[0]
        self.color_history.append(color)
        # print(f"rolled number is = {k} {color}")
        bets_result = calc_bets(bets, winning_bets)
        return bets_result

    def reset_history(self):
        self.roll_history = []
        self.color_history = []
        self.bet_history = []


# for each possible pts, get all bets as list

# Roulette

