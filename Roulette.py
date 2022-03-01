import numpy as np
import pandas as pd


from util import append_side_bets, add_2to1, create_euro_roulette


class Roulette:
    def  __init__(self):
        # self.players = {}
        self.numbers = list(range(0, 37))
        self.wheel = create_euro_roulette()
        self.history = []

    def roll(self, bets):
        # After each roll, renew.
        # self.players = {}
        k = np.random.choice(self.numbers)
        self.history.append(k)
        odd_even, color, onethird, first_half, two2one = self.wheel[k]

        amt2take = []
        for bet, amt in bets:
            if bet == k:
                amt2take.append(amt*36)
            if (bet == odd_even) | (bet == color) | (bet == first_half):
                amt2take.append(amt*2)
            if (bet == onethird) | (bet == two2one):
                amt2take.append(amt*3)
        return sum(amt2take)

    def reset_history(self):
        self.history = []


# for each possible pts, get all bets as list

# Roulette

