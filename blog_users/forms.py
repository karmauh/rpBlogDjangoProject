from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile

class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
        
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
        
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        
        
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password' }))
    new_password1 = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password' }))
    new_password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password' }))
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
        

class EditCharacterForm(forms.ModelForm):
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    appearance = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    history = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    profile_pic = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    
    class Meta:
        model = Profile
        fields = ('age', 'appearance', 'history', 'profile_pic')


class CreateCharacterForm(forms.ModelForm):
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    appearance = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    history = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Profile
        fields = ('age', 'appearance', 'history', 'profile_pic')