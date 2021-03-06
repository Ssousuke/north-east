from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render
from backend.publication.models import Post, Category
from django.db.models import Q


def home_page(request):
    template_name = 'pages/index.html'
    publication = get_list_or_404(Post, publish=True)
    paginator = Paginator(publication, 6)
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
    list_post = Post.objects.filter(category__category__iexact=category)
    paginator = Paginator(list_post, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template_name, context)


def search(request):
    template_name = 'pages/search_result.html'
    if request.method == 'POST':
        searched = request.POST['searched']
        result_list = Post.objects.filter(
            Q(title__icontains=searched) |
            Q(description__icontains=searched) |
            Q(category__category__icontains=searched)
        )
        context = {
            'searched': searched,
            'result_list': result_list,
        }
        return render(request, template_name, context)
    else:
        return render(request, template_name)


def error_404(request, exception):
    return render(request, 'error/404.html')
