from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Profile
from .forms import PostForm, EditPostForm, AddCommentForm
from django.urls import reverse_lazy


#Ten widok wyświetla listę wszystkich postów, uporządkowanych najpierw według najnowszego postu.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    

#Ten widok wyświetla szczegóły pojedynczego postu, w tym wszystkie komentarze z nim związane.
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = Profile.objects.all()
        return context
   

#Ten widok pozwala użytkownikowi stworzyć nowy post poprzez wypełnienie formularza. 
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
  

#Ten widok pozwala użytkownikowi edytować istniejący post poprzez wypełnienie formularza.
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'update_post.html'
   
  
#Ten widok pozwala użytkownikowi na usunięcie istniejącego postu.  
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    

#Ten widok pozwala użytkownikowi dodać nowy komentarz do postu poprzez wypełnienie formularza.
class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')