from django.shortcuts import render
from posts.models import Post

def home_page(request):
    recent_posts = Post.objects.filter().order_by('-dateTime')
    total_posts = Post.objects.count()
    return render(request, 'home.html', { 'recent_posts': recent_posts, 'total_posts': total_posts })
