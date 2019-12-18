from django import forms
from .models import FindStock

class NewSearch(forms.ModelForm):

    class Meta:
        model = FindStock

        fields = ('Symbol', 'Interval',)


