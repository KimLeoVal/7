from django import forms

from webapp.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = "__all__"


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'