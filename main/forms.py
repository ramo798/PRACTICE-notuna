from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('posttext',)
        widget=forms.TextInput(attrs={'class' : 'form-control'})
