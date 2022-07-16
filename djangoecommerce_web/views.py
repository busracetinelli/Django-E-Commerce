from django.shortcuts import render, redirect
from djangoecommerce_app.models import User, City, CompanyAddress, CompanyFeature,Card,Order, Company, ProductCategory,  Product, ProductImage, ProductBrand, Contact
from djangoecommerce_blog.models import Blog
from djangoecommerce_web.forms import ContactForm

def IndexView(request):
    context={
        "blog":Blog.objects.all()[:3],
        "product":Product.objects.all()
    }
    return render(request, 'web/index.html',context)


def ProductDetailView(request,id):
    context = {
        "product":Product.objects.get(id=id),
    }
    return render(request, 'web/product/product-detail.html',context)


def BlogDetailView(request,slug):
    context = {
        "blog":Blog.objects.get(slug=slug),
    }
    return render(request, 'web/blog-single.html',context)


def ContactView(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        Contact = form.save(commit=True)
        return redirect("djangoecommerce_web:contact")
    context = {
        "form": form
    }
    return render(request, 'web/contact.html',context)
