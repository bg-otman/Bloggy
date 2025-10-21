from django.shortcuts import render, redirect
from .models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def posts_list(request):
	posts = Post.objects.all().order_by("-dateTime")
	context = { 'posts' : posts }
	return render(request, 'posts/posts_list.html', context)

def post_page(request, slug):
	post = get_object_or_404(Post, slug=slug)
	context = { 'post' : post }
	return render(request, 'posts/post_page.html', context)

@login_required(login_url="users:login")
def new_post(request):
	if request.method == 'POST':
		form = forms.CreatePost(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False) # used to return an instance of the model, but still not saved to database
			post.author = request.user
			post.save()
			return redirect("posts:list")
	else:
		form = forms.CreatePost()
	return render(request, 'posts/new_post.html', { 'form' : form })

@login_required(login_url="users:login")
def my_posts(request):
	posts = Post.objects.filter(author=request.user).order_by("-dateTime")
	return render(request, 'posts/my_posts.html', { 'posts' : posts })

@login_required(login_url="users:login")
def delete_post(request):
	if request.method == 'POST':
		slug = request.POST.get('slug')
		user = request.user
		if user:
			post = Post.objects.get(slug=slug)
			if post:
				try:
					post.delete()
				except DoesNotExist:
					print("Error in deleting post with slug ", slug)
	posts = Post.objects.filter(author=request.user).order_by("-dateTime")
	return render(request, 'posts/my_posts.html', { 'posts' : posts })

@login_required(login_url="users:login")
def update_post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	form = forms.CreatePost(request.POST or None, request.FILES, instance=post)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			post_url = "/posts/" + post.slug
			return redirect(post_url)
	else:
		form = forms.CreatePost(instance=post)
	context = { 'form': form , 'post' : post }
	return render(request, 'posts/update_post.html', context)
