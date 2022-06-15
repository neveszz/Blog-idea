from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author', 'category','summary','body')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Insert title here'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Here goes the summary of the post'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Here goes the body of the post'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category':forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','summary', 'body', 'title_tag')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Insert title here'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Here goes the summary of the post'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Here goes the body of the post'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'})
        }