from django import forms
from .models import Post, Comment

#Klasa PostForm jest klasą formularza Django, która służy do tworzenia formularza do tworzenia nowego postu. 
#Dziedziczy ona po klasie forms.ModelForm i jest związana z modelem Post. Pola formularza to: title, title_tag, author, body i snippet, 
#a każde pole ma przypisane określone widżety do stylizacji przy użyciu klas Bootstrap CSS.
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
        

#Klasa EditPostForm jest podobna do klasy PostForm, ale służy do edycji istniejącego postu.
#Dziedziczy ona również z klasy forms.ModelForm i jest związana z modelem Post. Pola formularza to: title, title_tag, body i snippet
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


#Klasa AddCommentForm jest klasą formularza Django, która służy do tworzenia formularza dodawania nowego komentarza.
#Dziedziczy ona również po klasie forms.ModelForm i jest związana z modelem Comment. Pola formularza to name i body
class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        ordering = ['date_added']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }