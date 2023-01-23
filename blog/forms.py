from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body', 'snippet')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type the title of the post...'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type the title tag of the post...'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post content...'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Briefly describe your post...'}),
        }
        
        
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type the title of the post...'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type the title tag of the post...'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe the post...'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Briefly describe your post...'}),
        }