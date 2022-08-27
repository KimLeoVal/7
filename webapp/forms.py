from django import forms
#
# from webapp.models import Poll, Choice
#
#
from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

#
# class ChoiceForm(forms.ModelForm):
#     class Meta:
#         model = Choice
#         fields = ['text']