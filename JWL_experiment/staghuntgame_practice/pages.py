from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time

class Instruction(Page):
    timeout_seconds = 30
    def is_displayed(self):
        return self.round_number == 1

class Instruction1(Page):
    timeout_seconds = 10

class MyPage(Page):
    timeout_seconds = 10
    form_model = 'player'
    form_fields = ['Truth']

    def vars_for_template(self):
        a=Constants.a_point[self.round_number-1]
        b=Constants.b_point[self.round_number-1]
        c=Constants.c_point[self.round_number-1]
        d=Constants.d_point[self.round_number-1]
        return dict(
            a=a,
            b=b,
            c=c,
            d=d,
        )

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time()+10

class MidWaitingPage(Page):
    def get_timeout_seconds(self):
        return self.participant.vars['expiry']-time.time()

class Results(Page):
    def is_displayed(self):
        return self.player.Truth == True

    def vars_for_template(self):
        if self.player.Truth == True:
            return dict(a="사슴", b=Constants.a_point[self.round_number - 1])
        else:
            return dict(a="토끼", b=Constants.b_point[self.round_number - 1])
        return dict(a=a,
                    b=b)

    timeout_seconds = 5

page_sequence = [Instruction, Instruction1, MyPage, MidWaitingPage, Results]
