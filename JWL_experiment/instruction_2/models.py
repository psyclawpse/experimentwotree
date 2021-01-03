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
    name_in_url = 'instruction_2'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ox1 = models.BooleanField(
        choices=[
            [True, "O"],
            [False, "X"]
        ],
        widget=widgets.RadioSelectHorizontal()
    )
    ox2 = models.BooleanField(
        choices=[
            [True, "O"],
            [False, "X"]
        ],
        widget=widgets.RadioSelectHorizontal()
    )
    ox3 = models.BooleanField(
        choices=[
            [False, "O"],
            [True, "X"]
        ],
        widget=widgets.RadioSelectHorizontal()
    )
    ox4 = models.BooleanField(
        choices=[
            [True, "O"],
            [False, "X"]
        ],
        widget=widgets.RadioSelectHorizontal()
    )
    money1 = models.IntegerField(
    )


