from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = [
        'Age',
        'Gender',
        'Major',
        'Year',
        'InequityAversion1',
        'InequityAversion2',
        'InequityAversion3',
        'SubjectiveSES',
        'Explanation',
        'ExplanationT',
        'Undergrad'
    ]


page_sequence = [MyPage]
