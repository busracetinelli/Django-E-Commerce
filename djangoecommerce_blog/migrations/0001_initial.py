# Generated by Django 2.0.9 on 2019-04-15 15:32

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Başlık')),
                ('slug', models.SlugField(max_length=130, unique=True)),
                ('content', ckeditor.fields.RichTextField(verbose_name='İçerik')),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='', verbose_name='Blog Thumbnail')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='Oluşum Tarihi')),
                ('status', models.CharField(choices=[('private', 'Özel'), ('justLink', 'Sadece Link'), ('public', 'Herkese Açık')], max_length=15, verbose_name='Durum')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı Adı')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Bloglar',
            },
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Kategori')),
                ('category_slug', models.SlugField(max_length=130, unique=True)),
                ('category_tubnail', models.FileField(blank=True, null=True, upload_to='', verbose_name='Kategori Tubnailı')),
            ],
            options={
                'verbose_name': 'Blog Kategorisi',
                'verbose_name_plural': 'Blog Kategorileri',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ad Soyad')),
                ('email', models.EmailField(max_length=50, verbose_name='Mail')),
                ('subject', models.CharField(max_length=200, verbose_name='Başlık')),
                ('message', ckeditor.fields.RichTextField(verbose_name='Mesaj')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='Oluşum Tarihi')),
            ],
            options={
                'verbose_name': 'İletişim',
                'verbose_name_plural': 'İletişimler',
            },
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(max_length=120, verbose_name='Hashtag')),
            ],
            options={
                'verbose_name': 'Hashtag',
                'verbose_name_plural': 'Hashtagler',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoecommerce_blog.BlogCategory', verbose_name='Kategori'),
        ),
        migrations.AddField(
            model_name='blog',
            name='hashtag',
            field=models.ManyToManyField(blank=True, to='djangoecommerce_blog.Hashtag', verbose_name='Blog Hashtagleri'),
        ),
    ]