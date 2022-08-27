from django import forms
#
# from webapp.models import Poll, Choice
#
#
from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

#
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product','text','score']