# Generated by Django 3.2.8 on 2021-11-07 00:02

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
                ('category', models.CharField(max_length=80, verbose_name='Categoria')),
                ('description', models.CharField(max_length=255, verbose_name='Descrição')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='category', unique=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
                ('tag', models.CharField(max_length=100, verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('description', models.CharField(blank=True, max_length=330, verbose_name='Descrição')),
                ('body', models.TextField(verbose_name='Matéria')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True)),
                ('category', models.ForeignKey(help_text='Selecione a categoria que mais se aproxima do assunto.', max_length=20, on_delete=django.db.models.deletion.DO_NOTHING, to='publication.category', verbose_name='Categoria')),
                ('tag', models.ManyToManyField(help_text='Selecione algumas palavras chaves que façam referência ao assunto.', max_length=20, to='publication.Tag', verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Postagem',
                'verbose_name_plural': 'Postagens',
                'ordering': ['-updated_at'],
            },
        ),
    ]
