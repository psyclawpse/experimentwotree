from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import time

class Instruction(Page):
    timeout_seconds = 5
    def is_displayed(self):
        return self.round_number == 1

class ContributionLook(Page):
    form_model = 'player'
    form_fields = ['contribution']
    timeout_seconds = 10
    def is_displayed(self):
        return self.round_number == 7

    def before_next_page(self):
        player = self.player
        if self.timeout_happened:
            self.player.contribution = c(0)
            self.player.xyz = True

        player.contribution1_bot1 = c(53)
        player.contribution1_bot2 = c(53)
        player.contribution1_bot3 = c(53)

        player.payoff = c(0)
        self.participant.vars['expiry'] = time.time() + 10

class AnotherWaitingLook(Page):
    def is_displayed(self):
        return self.round_number == 7

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

class RetaliationLook(Page):
    def is_displayed(self):
        return self.round_number == 7

    form_model = 'player'
    form_fields = ['Retaliation_player', 'Retaliation_amount']

    def vars_for_template(self):
        a = self.player.contribution
        b = self.player.contribution1_bot1
        c = self.player.contribution1_bot2
        d = self.player.contribution1_bot3
        return dict(
            a=a,
            b=b,
            c=c,
            d=d
        )

class WaitingLook(Page):
    def is_displayed(self):
        return self.round_number == 7

    timeout_seconds = random.randint(7,10)

class ResultsLook(Page):
    def is_displayed(self):
        return self.round_number == 7

    timeout_seconds = 5

    def vars_for_template(self):
        a = self.player.contribution
        c = self.player.Retaliation_amount
        return dict(
            a=a,
            c=c
        )

class Contribution(Page):
    form_model = 'player'
    form_fields = ['contribution']
    timeout_seconds = 10

    def is_displayed(self):
        return self.round_number != 7

    def constrain(self, contribution):
        if contribution < 0 :
            return c(0)
        else:
            return contribution

    def before_next_page(self):
        player = self.player
        if self.timeout_happened:
            self.player.contribution = c(0)
            self.player.xyz = True

        player.contribution_bot1 = self.constrain(random.randint(2, 10)*5 + player.contribution)
        player.contribution_bot2 = self.constrain(random.randint(-10, -2)*5 + player.contribution)
        player.contribution_bot3 = self.constrain(random.randint(-1, 1)*5 + player.contribution)

        player.payoff = (player.contribution +
                         player.contribution_bot1 +
                         player.contribution_bot2 +
                         player.contribution_bot3
                        ) * 1.6 / 4 + Constants.endowment - player.contribution

        self.participant.vars['expiry'] = time.time() + 10
        self.participant.vars['people'] = [player.contribution_bot1, player.contribution_bot2, player.contribution_bot3]
        random.shuffle(self.participant.vars['people'])
        self.player.participant_vars_dump = str(self.participant.vars['people'])


class AnotherWaiting(Page):
    def is_displayed(self):
        return self.round_number != 7

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

class Retaliation(Page):
    def is_displayed(self):
        return self.round_number != 7
    form_model = 'player'
    form_fields = ['Retaliation_player', 'Retaliation_amount']

    def vars_for_template(self):
        a = self.player.contribution
        b = self.participant.vars['people'][0]
        c = self.participant.vars['people'][1]
        d = self.participant.vars['people'][2]
        return dict(
            a=a,
            b=b,
            c=c,
            d=d
        )

class Waiting(Page):
    def is_displayed(self):
        return self.round_number != 7
    timeout_seconds = random.randint(7,10)

class Results(Page):
    def is_displayed(self):
        return self.round_number != 7
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


class FinalResults(Page):
    def vars_for_template(self):
        a = self.participant.payoff
        return dict(
            a=a
        )

    def is_displayed(self):
        return self.round_number == 11


page_sequence = [Instruction, ContributionLook, AnotherWaitingLook, RetaliationLook, WaitingLook, ResultsLook, Contribution, AnotherWaiting, Retaliation, Waiting, Results, FinalResults]