from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField


def slugify_function(content):
    return content.replace('_', '-').lower()


class Base(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Data de Atualização')

    class Meta:
        abstract = True


class Category(Base):
    category = models.CharField(max_length=80, verbose_name='Categoria')
    description = models.CharField(max_length=255, verbose_name='Descrição')
    slug = AutoSlugField(populate_from='category', unique=True, editable=False)

    def __str__(self) -> str:
        return f'{self.category}'

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-updated_at']


class Tag(Base):
    tag = models.CharField(max_length=100, verbose_name='Tags')

    def __str__(self) -> str:
        return f'{self.tag}'

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['-updated_at']


class Post(Base):
    title = models.CharField(max_length=100, verbose_name='Título')
    thumb = models.ImageField(upload_to='posts/thumb', blank=True, verbose_name='Thumb')
    description = models.CharField(
        max_length=330, blank=True, verbose_name='Descrição')
    body = models.TextField(verbose_name='Matéria')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, max_length=20, verbose_name='Categoria',
                                 help_text='Selecione a categoria que mais se aproxima do assunto.')
    tag = models.ManyToManyField(Tag, max_length=20, verbose_name='Tag',
                                 help_text='Selecione algumas palavras chaves que façam referência ao assunto.')
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    publish = models.BooleanField(default=False, verbose_name='Publicar?')

    def get_absolute_url(self):
        return reverse('publication:detail', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
        ordering = ['-updated_at']
