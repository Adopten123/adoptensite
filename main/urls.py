from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.test2, name='home'),
    path('about/', views.about, name='about'),
    path('add_article/', views.add_article, name='add_article'),
    path('contacts/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('categories/<int:category_id>/', views.categories, name='categories'),
    path('categories/<slug:category_slug>/', views.categories_by_slug, name='categories_by_slug'),
    path('category/<int:category_id>/', views.show_category, name='category'),
    path('languages/<str:language_slug>/', views.language, name='languages'),
    path('archive/<year4:year>/', views.archive, name='archive'),
]

