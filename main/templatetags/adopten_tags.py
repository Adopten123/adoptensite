from django import template
import main.views as views

register = template.Library()

@register.simple_tag()
def get_categories():
    return views.categories_db

@register.inclusion_tag('main/list_categories.html')
def show_categories(category_selected=0):
    categories = views.categories_db
    return {'categories': categories, 'category_selected': category_selected}