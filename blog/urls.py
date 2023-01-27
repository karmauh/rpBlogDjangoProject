from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('update_post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]
