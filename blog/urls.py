from django.urls import path
from . import views

app_name ='blog'

urlpatterns = [
    path('',views.posts,name='posts'),
    path('about/',views.about,name='about'),
   
    path('post/details/<int:blog_id>',views.post,name='post'),
    path('add-post',views.add_post,name='add_post'),
    path('delete-post/<int:id>',views.delete_post,name='delete_post'),
    path('edit-post/<int:id>',views.edit_post,name='edit_post'),
]