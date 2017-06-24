from django import forms
from .models import Question, Answer

class GameForm(forms.Form):
    questions = Question.objects.all()

    question_one = forms.ModelChoiceField(
        queryset=questions[0].get_answers(),
        widget=forms.RadioSelect,
        empty_label=None,
        label=questions[0].question_text,
    )

    question_two = forms.ModelChoiceField(
        queryset=questions[1].get_answers(),
        widget=forms.RadioSelect,
        empty_label=None,
        label=questions[1].question_text,
    )

    question_three = forms.ModelChoiceField(
        queryset=questions[2].get_answers(),
        widget=forms.RadioSelect,
        empty_label=None,
        label=questions[2].question_text,
    )

    question_four = forms.ModelChoiceField(
        queryset=questions[3].get_answers(),
        widget=forms.RadioSelect,
        empty_label=None,
        label=questions[3].question_text,
    )
