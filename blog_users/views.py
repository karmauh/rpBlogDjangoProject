from django.shortcuts import render, get_object_or_404
from django.http import request
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignupForm, EditProfileForm, PasswordChangingForm, EditCharacterForm, CreateCharacterForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView, ListView
from blog.models import Profile

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
    
class UserChangeView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
    

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home')
    
    
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/show_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        
        return context
    

# class ShowOtherProfilePageView(DetailView):
#     model = Profile
#     template_name = 'show_other_profile.html'
#     context_object_name = 'users'
def ShowOtherProfilePageView(request):
    users = Profile.objects.all()
    return render(request, 'registration/show_other_profile.html', {'users': users})


class EditCharacterView(generic.UpdateView):
    model = Profile
    form_class = EditCharacterForm
    template_name = 'registration/edit_character.html'
    success_url = reverse_lazy('all_profiles')


class CreateCharacterView(CreateView):
    model = Profile
    form_class = CreateCharacterForm
    template_name = 'registration/create_character.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)