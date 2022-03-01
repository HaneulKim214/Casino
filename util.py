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

def create_euro_roulette():
    wheel = {}
    for i in range(37):
        lst = []
        if i == 0:
            lst.append("green")
            wheel[i] = lst
            continue
        elif i % 2 == 0:
            lst.append("even")
            lst.append("red")
            lst = append_side_bets(lst, i)
            lst = add_2to1(lst, i)
        else:
            lst.append("odd")
            lst.append("black")
            lst = append_side_bets(lst, i)
            lst = add_2to1(lst, i)
        wheel[i] = lst
    return wheel