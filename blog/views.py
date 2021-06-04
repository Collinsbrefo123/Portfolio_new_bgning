from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Blogs


def all_blogs(request):
    blogs = Blogs.objects.order_by('-date')[:5]
    return render(request, 'blogs/all_blogs.html', {'blogs': blogs})


def details(request, blog_id):
    blogs = get_object_or_404(Blogs, pk=blog_id)

    return render(request, 'blogs/each_blog.html', {'blogs':blogs})
