from django import template
from main.models import Category, Article

register = template.Library()


@register.simple_tag()
def get_categories():
    categories = Category.objects.all()
    return categories
