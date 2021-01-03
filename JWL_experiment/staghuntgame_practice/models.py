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
    name_in_url = 'staghuntgame_practice'
    players_per_group = None
    num_rounds = 1

    a_point = [5]
    b_point = [4]
    c_point = [4]
    d_point = [1]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Truth = models.BooleanField()

