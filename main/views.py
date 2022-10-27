from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def home_view(request):
    context = {
        "articles": Article.objects.order_by('-created_at')[:3],
        "categories": Category.objects.all()
    }
    return render(request, 'main/home.html', context)


def category_view(request, slug):
    context = {}
    category = Category.objects.get(slug=slug)
    articles = Article.objects.filter(category=category)
    context['category'] = category
    context['articles'] = articles
    return render(request, 'main/category.html', context)


def detail_view(request, slug):
    context = {}
    article = Article.objects.get(slug=slug)
    article.views += 1
    article.save()
    articles = Article.objects.all().values_list('views', flat=True)
    avg_articles = sum(articles) // len(articles)
    print(articles)
    context['article'] = article

    context['articles'] = Article.objects.filter(views__lte=avg_articles)[:3]

    return render(request, 'main/article_detail.html', context)
