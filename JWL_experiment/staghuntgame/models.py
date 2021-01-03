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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'staghuntgame'
    players_per_group = None
    num_rounds = 5

    a_point = [4, 5, 4, 4, 4]
    b_point = [3, 4, 2.5, 3.5, 3]
    c_point = [3, 4, 2.5, 3.5, 3]
    d_point = [0, 1, 0, 0, 0]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Truth = models.BooleanField()

