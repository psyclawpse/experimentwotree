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
    name_in_url = 'aftermath'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Age = models.IntegerField(label = '당신의 나이는? (만 나이)')
    Gender = models.StringField(
        label = '당신의 성별은?',
        choices = [
            '남성',
            '여성',
            '기타 혹은 답변하고 싶지 않음'
        ],
        widget = widgets.RadioSelectHorizontal()
    )
    Major = models.StringField(
        label = '당신이 속한 학과는?'
    )
    Year = models.StringField(
        label = '2020년 현재 몇 학년이십니까?',
        choices = ["1학년",
                   "2학년",
                   "3학년",
                   "4학년",
                   "5학년 이상"
                   ]
    )
    InequityAversion1 = models.IntegerField(
        max=10,
        min = 1,
        widget = widgets.SliderInput
    )
    InequityAversion2 = models.IntegerField(
        max=10,
        min=1,
        widget=widgets.SliderInput
    )
    InequityAversion3 = models.IntegerField(
        max=10,
        min=1,
        widget=widgets.SliderInput
    )
    SubjectiveSES = models.IntegerField(
        label = "'1'이 우리 사회에서 가장 낮은 계층, '10'이 우리 사회에서 가장 높은 계층이라고 할 때,  귀하는 어디에 속한다고 생각하십니까?\n(이때의 기준은 주관적인 것으로, 스스로의 기준에 의거하여 대답해주시면 됩니다.)",
        max = 10,
        min = 1,
        widget = widgets.SliderInput
    )
    Explanation = models.BooleanField(
        label = "추후에 실험에 대한 설명을 받기를 바라십니까?",
        choices = [
            [True, '예'],
            [False, '아니오']
       ]
    )
    ExplanationT = models.StringField(
        label = "위의 질문에 '예'라고 대답한 경우, 실험 설명을 받을 이메일을 적어주세요.",
        blank = True
    )
    Undergrad = models.StringField(
        label = "현재 어느 과정을 밟고 계신 지 응답하여 주시길 바랍니다.",
        choices =
            ["학부과정",
             "석사과정",
             "박사과정",
             "석박사통합과정"]
        )