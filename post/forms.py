from django import forms 

from .models import Post 

class PostCreate(forms.ModelForm):
    body = forms.CharField(widget=forms.widgets.Textarea(attrs={"class":'post-add',"id":"profile-post-input"}))
    class Meta :
        model = Post 
        fields = ['body']