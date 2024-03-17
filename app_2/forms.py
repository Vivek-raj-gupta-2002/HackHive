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
<<<<<<< HEAD
        widget=forms.TextInput(attrs={'class': 'add-your-calendly-link'}))
=======
        widget=forms.URLInput(attrs={'class': 'add-your-calendly-link'}))
>>>>>>> 2ae0c43e33141473d07fdc5883f0ca4ab744929a
    
    about=forms.CharField(
        widget=forms.TextInput(attrs={'class':'about'})
    )

    submit=forms.CharField(
        widget=forms.URLInput(attrs={'class':'submit'})
    )
