from django.urls import path, include
from .import views

urlpatterns = [
     path('', views.index, name="index"),
     path('blog/', views.blog, name="post-list"),
     path('post/<id>/', views.post, name="post-detail"),
     path('search/', views.search, name='search'),
     path('tinymce/', include('tinymce.urls')),
     path('post/<id>/update', views.post_update, name="post-update"),
     path('post/<id>/delete', views.post_delete, name="post-delete"),
     path('create/', views.post_create, name="post-create"),
     
]
