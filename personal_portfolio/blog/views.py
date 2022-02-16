from django.shortcuts import render, get_object_or_404
from blog import models

def all_blogs(request):
    blogs = models.Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(models.Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
