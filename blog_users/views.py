from django.shortcuts import render, get_object_or_404
from django.http import request
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignupForm, EditProfileForm, PasswordChangingForm, EditCharacterForm, CreateCharacterForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView
from blog.models import Profile


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
    

#PasswordsChangeView to oparty na klasach widok, który pozwala użytkownikom zmieniać własne hasła. 
#Używa klasy formularza PasswordChangingForm do obsługi aktualizacji informacji o haśle użytkownika oraz wbudowanego szablonu zmiany hasła Django
#do wyświetlenia formularza użytkownikowi. Gdy użytkownik prześle formularz i hasło zostanie pomyślnie zmienione, użytkownik zostanie przekierowany na stronę główną.
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home')
    

#ShowProfilePageView to oparty na klasie widok, który pokazuje stronę profilu użytkownika.
#Używa modelu Profile do pobierania informacji o profilu użytkownika oraz szablonu show_profile.html do wyświetlania informacji użytkownikowi.
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/show_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        
        return context
    

#ShowOtherProfilePageView jest widokiem opartym na funkcji,
#który pokazuje wszystkie profile użytkowników. Wykorzystuje model Profile do pobierania wszystkich profili użytkowników
#oraz szablon show_other_profile.html do wyświetlania informacji użytkownikowi.
def ShowOtherProfilePageView(request):
    users = Profile.objects.all()
    return render(request, 'registration/show_other_profile.html', {'users': users})


#EditCharacterView jest opartym na klasach widokiem, który pozwala użytkownikom edytować ich własne postacie.
#Używa on klasy formularza EditCharacterForm do obsługi aktualizacji informacji o postaci oraz szablonu edit_character.html
#do wyświetlenia formularza użytkownikowi.
class EditCharacterView(generic.UpdateView):
    model = Profile
    form_class = EditCharacterForm
    template_name = 'registration/edit_character.html'
    success_url = reverse_lazy('all_profiles')


#CreateCharacterView jest opartym na klasach widokiem, który pozwala użytkownikom na stworzenie nowej postaci.
#Używa on klasy formularza CreateCharacterForm do obsługi tworzenia nowych postaci oraz szablonu
#create_character.html do wyświetlenia formularza użytkownikowi. Gdy użytkownik prześle formularz i
#postać zostanie pomyślnie utworzona, zostanie on przekierowany na stronę all_profiles.
#Widok ustawia również atrybut użytkownika na instancji formularza na bieżącego użytkownika
#przed zapisaniem formularza, tak aby nowa postać była powiązana z bieżącym użytkownikiem.
class CreateCharacterView(CreateView):
    model = Profile
    form_class = CreateCharacterForm
    template_name = 'registration/create_character.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)