from django import forms
from .helpers import *
import re


class QForm(forms.Form):
    venue_city = forms.CharField(required=False)
    venue_region = forms.CharField(required=False)
    venue_country = forms.CharField(required=False)
    q = forms.CharField(required=False, label='Keywords')
    categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=get_categories(), required=True)
    popular = forms.BooleanField(required=False)
     
    def clean_categories(self):
        data = self.cleaned_data['categories']
        print("Cleaning categories")
        print(self.cleaned_data['categories'])
        if len(data) > 3 or len(data)==0:
            raise forms.ValidationError("You can select between 1 and 3 categories.")
        return data
    
    def clean_venue_city(self):
        data = self.cleaned_data['venue_city']
        if check_names(data):
            raise forms.ValidationError("Please enter valid city name.")
        return data
    
    def clean_venue_region(self):
        data = self.cleaned_data['venue_region']
        if check_names(data):
            raise forms.ValidationError("Please enter valid region name.")
        return data
    
    def clean_country(self):
        data = self.cleaned_data['country']
        if check_names(data):
            raise forms.ValidationError("Please enter valid country name.")
        return data
    
    def clean_keywords(self):
        data = self.cleaned_data['keywords']
        if check_names(data):
            raise forms.ValidationError("Please enter valid keywords.")
        return data
