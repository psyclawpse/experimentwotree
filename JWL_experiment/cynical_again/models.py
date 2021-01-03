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
import math

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'cynical_again'
    players_per_group = None
    num_rounds = 11
    endowment = c(100)

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    contribution = models.CurrencyField(min=0, max = Constants.endowment)
    contribution1 = models.CurrencyField(min=0, max = Constants.endowment)

    contribution_bot1 = models.CurrencyField()
    contribution_bot2 = models.CurrencyField()
    contribution_bot3 = models.CurrencyField()

    contribution1_bot1 = models.CurrencyField()
    contribution1_bot2 = models.CurrencyField()
    contribution1_bot3 = models.CurrencyField()

    Retaliation_amount = models.IntegerField(
        blank=True,
        min=0,
        max=10,
        initial=0,
        widget=widgets.SliderInput(),
        label="처벌하는 데 포인트를 얼마나 사용하시겠습니까?"
    )

    xyz = models.BooleanField()

    Retaliation_player = models.StringField(
        label="누구를 처벌하시겠습니까?",
        blank=True,
        choices=["Player 2", "Player 3", "Player 4"]
    )

    participant_vars_dump = models.LongStringField()

    def truncate(self, decimals = -3):
        multiplier = 10 ** decimals
        return int(self.payoff * 10 * 2 * multiplier)/multiplier + 5000

class Subsession(BaseSubsession):
   pass