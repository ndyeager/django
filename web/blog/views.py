from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def index(request):
	latest_blog_list = Post.objects.order_by('-pub_date')[:5]
	output = ', '.join([p.blog_text for p in latest_blog_list])

	return HttpResponse(output)
