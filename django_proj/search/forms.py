from django import forms
from .helpers import *


class QForm(forms.Form):
    venue_city = forms.CharField(required=False)
    venue_region = forms.CharField(required=False)
    venue_country = forms.CharField(required=False)
    keywords = forms.CharField(required=False)
    categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=get_categories(), required=True)
     
    def clean_categories(self):
        data = self.cleaned_data['categories']
        print('here is cleaned data:')
        print(data)
        if len(data) > 3 or len(data)==0:
            raise forms.ValidationError("You can select between 1 and 3 categories.")
        return data