"""
For debugging python scripts within Casino package.
"""

import numpy as np
import pandas as pd

from Roulette import Roulette
from roulette_strategies import double_till_win_2x
from util import run_roulette_simulation


# Strategy 1 : bet on 1/2
n_trials = 10
start_wallet = 10000
init_bets = [("red", 10)]
min_bet = 10
sim_df_lst = []
max_bet_list = [np.inf]

for max_bet in max_bet_list:
    euro_roulette = Roulette(min_bet, max_bet, "euro")

    for i_sim, n_rolls in enumerate([30, 50, 100, 500, 1000, 2000, 5000]):
        print(f" ========================= {max_bet}max_bet-{n_rolls}rolls-{i_sim}th simluation ===========================")
        sim_df = run_roulette_simulation(euro_roulette, n_trials, n_rolls, start_wallet, init_bets)
        sim_df["simulation"] = [f"{i_sim}sim_{n_trials}trials_{n_rolls}rolls_{max_bet}maxbet"]*len(sim_df)
        sim_df_lst.append(sim_df)

simulations_df = pd.concat(sim_df_lst)