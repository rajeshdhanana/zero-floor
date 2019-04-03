from django import forms

class MonthlyCollectionsForm(forms.ModelForm):
    class Media:
        js = ('monthlyCollections.js')