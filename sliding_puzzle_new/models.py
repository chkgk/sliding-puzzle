from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


import random


author = 'Yang Zhong'

doc = """
Sliding Puzzle experiment. Different time pressure levels are imposed. 
"""


class Constants(BaseConstants):
    name_in_url = 'sliding_puzzle'
    players_per_group = None
    num_rounds = 1
    #endowment=c(10)    # Every player is given 10 euro at the beginning of each game. Every round,
                       # a certain amount of money is deducted per 10 seconds. In the last 5 seconds
                       # of every ten seconds, the clock blinks in red. The clock and amount of money
                       # left are always shown on screen. (Or deduction of money per move).


class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    puzzle_solved = models.BooleanField(initial=False)
    move_history = models.LongStringField()
    payoff_display = models.FloatField()
    num_of_moves = models.IntegerField()
    board_history = models.LongStringField()



class Group(BaseGroup):
    pass


