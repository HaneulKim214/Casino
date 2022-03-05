"""
Various roulette strategies.

"""



def double_till_win_2x(bet, bet_amt, new_amt, init_amt=10):
    """
    Bet on 2x payout and double bet when lost until win. If max bet reached, stop.

    !!! need fix: currently only one bet at a time => one tuple in bets_result

    :parameter:
    bet : string or int
          bets you've made.
    bet_amt : int
              amount you've bet.
    new_amt : int
              result amount after roll.
    init_amt : int
               starting bet amount.

    :return:
    new_bets : list of tuples
    """
    init_amt = 10
    if new_amt == 0: # lose scenario: double money.
        bets = [(bet, bet_amt * 2)]
    else: # win scenario: start from initial amount.
        bets = [(bet, init_amt)]
    return bets