from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Title')
    slug = models.SlugField(unique=True, null=True, verbose_name='Slug')

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Category(pk={self.pk}, title={self.title})'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Article(models.Model):
    image = models.ImageField(upload_to='article_images/', verbose_name='Image')
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='Title')
    description_lite = models.TextField(verbose_name='Description lite')
    description = RichTextField(verbose_name='Description')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='Category',
                                 related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    views = models.IntegerField(default=0, verbose_name='Views')
    slug = models.SlugField(unique=True, null=True)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Article(pk={self.pk}, title={self.title})'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-created_at', 'category']
