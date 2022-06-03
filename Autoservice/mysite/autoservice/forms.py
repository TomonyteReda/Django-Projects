from .models import ClientReview
from django import forms


class ClientReviewForm(forms.ModelForm):
    class Meta:
        model = ClientReview
        fields = ('content', 'order', 'reviewer',)
        widgets = {'order': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}
