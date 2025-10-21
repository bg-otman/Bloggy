from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
	path('', views.posts_list, name='list'),
	path('my_posts/', views.delete_post, name='delete_post'),
	path('my_posts/', views.my_posts, name='my_posts'),
	path('new_post/', views.new_post, name='new_post'),
	path('<slug:slug>/update/', views.update_post, name='update_post'),
	path('<slug:slug>/', views.post_page, name='page'),
]
