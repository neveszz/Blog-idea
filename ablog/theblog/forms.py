from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'author', 'title_tag')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Insert title here'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Here goes the body of the post'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'})
        }