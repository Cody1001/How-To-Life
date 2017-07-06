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

    question_five = forms.ModelChoiceField(
        queryset=questions[4].get_answers(),
        widget=forms.RadioSelect,
        empty_label=None,
        label=questions[4].question_text,
    )

    qustion_six = forms.ModelChoiceField(
        queryset=questions[5].get_answers(),
        widget=forms.RadioSelect,
        empty_label=None,
        label=questions[5].question_text,
    )

    question_seven = forms.ModelChoiceField(
        queryset=questions[6].get_answers(),
        widget=forms.RadioSelect,
        empty_label=None,
        label=questions[6].question_text,
    )

    question_eight = forms.ModelChoiceField(
        queryset=questions[7].get_answers(),
        widget=forms.RadioSelect,
        empty_label=None,
        label=questions[7].question_text,
    )

    question_nine = forms.ModelChoiceField(
        queryset=questions[8].get_answers(),
        widget=forms.RadioSelect,
        empty_label=None,
        label=questions[8].question_text,
    )

    question_ten = forms.ModelChoiceField(
        queryset=questions[9].get_answers(),
        widget=forms.RadioSelect,
        empty_label=None,
        label=questions[9].question_text,
    )
