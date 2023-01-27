from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Profile
from .forms import PostForm, EditPostForm, AddCommentForm
from django.urls import reverse_lazy

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = Profile.objects.all()
        return context
   
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = "__all__"
    #fields = ('title', 'body')
  
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'update_post.html'
    #fields = ('title', 'title_tag', 'body')
   
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    

class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'
    #fields = "__all__"
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')