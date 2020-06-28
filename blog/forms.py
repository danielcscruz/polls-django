from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
          'title': forms.Textarea(attrs={'rows':1,'cols':60}),
          'text': forms.Textarea(attrs={'rows':3, 'cols':60}),
        }