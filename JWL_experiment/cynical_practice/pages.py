from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import time

class Instruction(Page):
    timeout_seconds = 5
    def is_displayed(self):
        return self.round_number == 1

class Contribution(Page):
    form_model = 'player'
    form_fields = ['contribution']
    timeout_seconds = 10

    def constrain(self,contribution):
        if contribution < 0 :
            return c(0)
        else:
            return contribution

    def before_next_page(self):
        player = self.player
        if self.timeout_happened:
            self.player.contribution = c(0)
            self.player.xyz = True

        player.contribution_bot1 = random.randint(0, 20) * 5
        player.contribution_bot2 = random.randint(0, 20) * 5
        player.contribution_bot3 = random.randint(0, 20) * 5

        player.payoff = (player.contribution +
                         player.contribution_bot1 +
                         player.contribution_bot2 +
                         player.contribution_bot3
                        ) * 1.6 / 4 + Constants.endowment - player.contribution

        self.participant.vars['expiry'] = time.time() + 10

class AnotherWaiting(Page):
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

class Retaliation(Page):
    form_model = 'player'
    form_fields = ['Retaliation_player', 'Retaliation_amount']

    def vars_for_template(self):
        a = self.player.contribution
        b = self.player.contribution_bot1
        c = self.player.contribution_bot2
        d = self.player.contribution_bot3
        return dict(
            a=a,
            b=b,
            c=c,
            d=d
        )

    def is_displayed(self):
        return self.round_number == 1, 2, 3, 4, 5

class Waiting(Page):
    timeout_seconds = random.randint(7,10)


class Results(Page):
    timeout_seconds = 10
    def vars_for_template(self):
        a = self.player.contribution
        b = self.player.payoff
        c = self.player.Retaliation_amount
        d = self.player.payoff - self.player.Retaliation_amount
        e = 0
        return dict(
            a=a,
            b=b,
            c=c,
            d=d,
            e=e
        )

    def before_next_round(self):
        return self.player.payoff == self.player.payoff - self.player.Retaliation_amount


class FinalOK(Page):
    def vars_for_template(self):
        a = self.participant.payoff
        b= self.participant.payoff_plus_participation_fee()
        return dict(
            a=a,
            b=b,
        )

    def is_displayed(self):
        return self.round_number == 5

class Warning(Page):
    def is_displayed(self):
        return self.player.xyz == True

page_sequence = [Instruction, Contribution, AnotherWaiting, Warning, Retaliation, Waiting, Results, FinalOK]