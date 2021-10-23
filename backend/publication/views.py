from django.shortcuts import render
from backend.publication.models import Post


def home_page(request):
    template_name = 'pages/index.html'
    publication = Post.objects.all()
    context = {
        'publication': publication,
    }
    return render(request, template_name, context)
