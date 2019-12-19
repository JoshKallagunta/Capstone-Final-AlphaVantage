from django import forms
from .models import FindStock

#Model from, using the model FindStock 
#Creates a form with Symbol and Interval 
class NewSearch(forms.ModelForm):

    class Meta:
        model = FindStock

        fields = ('Symbol', 'Interval',)


