from django.shortcuts import render, get_object_or_404
from core.libs.corelib import request_get
from .models import Post, Category

@request_get
def blog(request):
    allpost = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts':allpost})

@request_get
def category(request, category_id):
    objcategory = get_object_or_404(Category,id=category_id)
    return render(request, 'blog/category.html', {'category':objcategory})
    