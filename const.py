"""
Storage for constant variables
"""

# multiples for each bet
BET_DICT = {"black": 2, "red": 2, "odd": 2, "even": 2, "1to18": 2, "19to36": 2,
            "first_12": 3, "second_12": 3, "third_12": 3, "left_2to1": 3, "mid2to1": 3, "right_2to1": 3}
for i in range(37):
    BET_DICT[i] = 36