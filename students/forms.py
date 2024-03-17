from django import forms
from . import models

class diaryForm(forms.ModelForm):
    class Meta:
        model = models.Diary
        fields = ['message', ] 

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['content', ]

        widget = {
            'content': forms.Textarea(attrs={'placeholder': "What’s on your mind ?", 'class': "whats-on-your-mind"})
        }
    
    



    
