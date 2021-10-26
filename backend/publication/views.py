from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from backend.publication.models import Post


def home_page(request):
    """
        :template_name = recebe o html a serem renderizado
        :publication = recebe os objetos a serem renderizados no html
        :paginator = recebe os objetos e a quantidade que vão ser renderizados
        : 

    """
    template_name = 'pages/index.html'

    publication = Post.objects.all()
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
