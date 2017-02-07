from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.filter().order_by('published_date')
	return render(request,'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
	post = get_object_or_404(Post, pk = post_id) #pk = primary key or name of field (id for example)
	return render(request, 'blog/post_detail.html', {'post': post})