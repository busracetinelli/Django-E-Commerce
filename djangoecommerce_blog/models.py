from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.db.models import Model,ForeignKey,CharField,DateTimeField,EmailField,TextField,ManyToManyField,SlugField,ImageField
from djangoecommerce_app.models import User


class Hashtag(Model):
    hashtag = CharField(max_length=120, verbose_name="Hashtag")

    class Meta:
        verbose_name = 'Hashtag'
        verbose_name_plural = 'Hashtagler'

    def __str__(self):
        return self.hashtag


class BlogCategory(Model):
    title = CharField(max_length=120, verbose_name="Kategori")
    category_slug = SlugField(unique=True, max_length=130)
    category_tubnail = ImageField(blank=True, null=True, verbose_name="Kategori Tubnailı")
    category_color = ColorField(default='#fe4c50')
    
    class Meta:
        verbose_name = 'Blog Kategorisi'
        verbose_name_plural = 'Blog Kategorileri'

    def __str__(self):
        return self.title


class Blog(Model):
    PAGE_STATUS=(
        ('private','Özel'),
        ('justLink','Sadece Link'),
        ('public','Herkese Açık'),
    )
    author = ForeignKey("djangoecommerce_app.User", on_delete=models.CASCADE, verbose_name="Kullanıcı Adı")
    title = CharField(max_length=120, verbose_name="Başlık")
    slug = SlugField(unique=True, max_length=130)
    content = RichTextField(verbose_name="İçerik")
    thumbnail = ImageField(verbose_name="Blog Thumbnail", upload_to='images/blog/thumbnail/', blank=True, null=True)
    created_date = DateTimeField(auto_now=True, verbose_name="Oluşum Tarihi")
    status = CharField(max_length=15,choices=PAGE_STATUS, verbose_name="Durum")
    category = ForeignKey('djangoecommerce_blog.BlogCategory', on_delete=models.CASCADE, verbose_name='Kategori')
    hashtag = ManyToManyField('djangoecommerce_blog.Hashtag', verbose_name='Blog Hashtagleri', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'
