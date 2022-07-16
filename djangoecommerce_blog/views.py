from django.shortcuts import render
from djangoecommerce_blog.models import BlogCategory
from djangoecommerce_blog.models import Blog,Hashtag

def BlogListView(request):
    context = {
        "blog": Blog.objects.all()
    }
    return render(request, 'blog/index.html', context)


def CategoryListView(request):

    return render(request, 'blog/category.html')


def HashtagListView(request,hashtag):
    hashtag = Hashtag.objects.get(hashtag=hashtag)
    blog = Blog.objects.filter(hashtag=hashtag)
    context = {
        "hashtag": hashtag,
        "blog": blog

    }
    return render(request, 'blog/hashtag.html',context)

def BlogDetailView(request,slug):
    context = {
        "blog": Blog.objects.get(slug=slug)
    }
    return render(request, 'blog/blog/blog-detail.html',context)
