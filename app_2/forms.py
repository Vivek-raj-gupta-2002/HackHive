from django import forms
from . import models

class profileForm(forms.ModelForm):
    name = forms.CharField(
       widget=forms.TextInput(attrs={'class': 'name'})
     )

    title =forms.CharField(
         widget=forms.TextInput(attrs={'class':'title'})
     )

    areaofexpertise=forms.CharField(
        widget=forms.TextInput(attrs={'class':'area-of-expertise'})
    )

    addyourcalendylink=forms.URLField(
        widget=forms.URLInput(attrs={'class': 'add-your-calendly-link'}))
    
    about=forms.CharField(
        widget=forms.TextInput(attrs={'class':'about'})
    )

    class Meta:
        model = models.profile
        exclude = ('user',)  # all fields of the
