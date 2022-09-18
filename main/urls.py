from django.urls import path
from .views import *
urlpatterns = [
    path('', home_view, name='home'),
    path('category/<slug:slug>/', category_view, name='category'),
    path('<slug:slug>/', detail_view, name='article_detail'),
]
