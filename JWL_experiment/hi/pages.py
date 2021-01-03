from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Explanation(Page):
    pass

class Page1(Page):
    pass

class Page2(Page):
    pass

class Page3(Page):
    pass

class Quiz(Page):
    form_model = 'player'
    form_fields = ['ox1', 'ox2', 'ox3', 'ox4', 'money1']

    def int_to_bool(self):
        if self.money1 == 160:
            return self.money1 == 1
        else:
            return self.money1 == 0

class QuizAnswer(Page):
    pass

page_sequence = [Explanation, Page1, Page2, Page3, Quiz, QuizAnswer]
