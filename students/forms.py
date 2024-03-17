from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['content', ]

        widget = {
            'content': forms.Textarea(attrs={'placeholder': "What’s on your mind ?", 'class': "whats-on-your-mind"})
        }
    
    



    
