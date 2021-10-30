from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from backend.publication.models import Post, Category


def home_page(request):
    template_name = 'pages/index.html'
    publication = Post.objects.all()
    paginator = Paginator(publication, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template_name, context)


def detail(request, slug):
    template_name = 'pages/detail.html'
    detail = get_object_or_404(Post, slug=slug)
    context = {
        'detail': detail,
    }
    return render(request, template_name, context)


def category(request):
    category = Category.objects.all()
    template_name = 'pages/category.html'
    context = {
        'category': category
    }
    return render(request, template_name, context)


def post_category(request, category):
    template_name = 'pages/index.html'
    page_obj = Post.objects.filter(category__category__iexact=category)
    context = {
        'page_obj': page_obj,
    }
    print(context)
    return render(request, template_name, context)
