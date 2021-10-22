from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    body = models.TextField(verbose_name='Matéria')
    category = models.CharField(max_length=20, verbose_name='Categoria',
                                help_text='Selecione a categoria que mais se aproxima do assunto.')
    tag = models.CharField(max_length=20, verbose_name='Tag',
                           help_text='Selecione algumas palavras chaves que façam referência ao assunto.')
    upload_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
        ordering = ['-updated_at']

