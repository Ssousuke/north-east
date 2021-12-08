from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('login/admin/', admin.site.urls),
    path('', include('backend.publication.urls', namespace='publication')),
    path('publications/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'Painel de Controle'
admin.site.index_title = 'Bem-vindo a página de administração!'
admin.site.site_title = 'Painel de Controle'

handler404 = 'backend.publication.views.error_404'
