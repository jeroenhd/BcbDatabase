from django import forms


class SearchForm(forms.Form):
    """Search form"""

    terms = forms.CharField(label="Search terms")
    """The search terms"""
