"""
Utility functions for Casino package.

"""


import pandas as pd
import plotly.graph_objects as go

from const import BET_DICT
from roulette_strategies import double_till_win_2x


def append_side_bets(lst, i):
    """
    Add all side bets to appropriate numbers

    Parameters
    ----------
    lst : list
          list of bets a number has so far
    i : int
        current number
    """
    if i <= 13:
        lst.append("first_12")
    elif 13 <= i <= 24:
        lst.append("second_12")
    else:
        lst.append("third_12")
    if i <= 18:
        lst.append("1to18")
    else:
        lst.append("19to36")
    return lst

def add_2to1(lst, i):
    if i in list(range(1, 35, 3)):
        lst.append("left_2to1")
    elif i in list(range(2, 36, 3)):
        lst.append("mid_2to1")
    else:
        lst.append("right_2to1")
    return lst

def calc_bets(bets, winning_bets):
    """
    From all bets, return result bet with appropriate bet multiple.

    Parameters
    -----------
    bets: list of tuples
          ex : [(bet_position, bet_amount, new_amount)]
    """
    bets_result = []
    for bet, bet_amt in bets:
        if bet in winning_bets:
            multiply_bet_by = BET_DICT[bet]
            new_amt = bet_amt * multiply_bet_by
        else:
            new_amt = 0
        bets_result.append((bet, bet_amt, new_amt))
    return bets_result


def create_wheel(type):
    wheel = {}
    for i in range(37):
        lst = []
        if i == 0:
            if type == "us":
                lst.append("green")
                wheel[i] = lst
            lst.append("green")
            wheel[i] = lst
            continue
        elif i % 2 == 0:
            lst.append("red")
            lst.append("even")
            lst = append_side_bets(lst, i)
            lst = add_2to1(lst, i)
        else:
            lst.append("black")
            lst.append("odd")
            lst = append_side_bets(lst, i)
            lst = add_2to1(lst, i)
        wheel[i] = lst
    return wheel


def run_roulette_simulation(euro_roulette, n_trials, n_rolls, start_wallet, init_bets):
    sim_df_lst = []

    for ith_trial in range(n_trials):
        wallet_history = []
        wallet = start_wallet
        bets = init_bets
        euro_roulette.reset_history()

        for ith_roll in range(1, n_rolls + 1):
            bets_result = euro_roulette.roll(bets)

            # Only for first tuple, need fix for multiple bets.
            bet, bet_amt, new_amt = bets_result[0]
            wallet += new_amt - bet_amt
            wallet_history.append(wallet)

            # new bets following double_till_win_2x strategy.
            bets = double_till_win_2x(bet, bet_amt, new_amt)
            if bets[0][-1] > euro_roulette.max_bet:
                print("That's enough haneul... Please stop")
                break
            if wallet < 0:
                print("No choice, time to go home...")

        df = pd.DataFrame({"trial": [ith_trial] * ith_roll,
                           "wallet": wallet_history,
                           "bet": euro_roulette.bet_history,
                           "color": euro_roulette.color_history,
                           "roll": euro_roulette.roll_history,
                           "ith_roll": list(range(ith_roll)),
                           "max_bet": [euro_roulette.max_bet] * ith_roll})
        sim_df_lst.append(df)
    sim_df = pd.concat(sim_df_lst)
    return sim_df