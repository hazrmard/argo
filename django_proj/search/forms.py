from django import forms
from .models import Query

class QueryForm(forms.ModelForm):

    class Meta:
        model = Query
        fields = ('city', 'region', 'country', 'categories', 'popular',)

class QForm(forms.Form):
    categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=Query().get_categories())