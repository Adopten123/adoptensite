from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse

menu = [
    {'title' : 'About', 'url_name' : 'about'},
    {'title' : 'Add Article', 'url_name' : 'add_article'},
    {'title' : 'Contact Info', 'url_name' : 'contact'},
    {'title' : 'Login', 'url_name' : 'login'},
]
data_db = [
    {'id': 1, 'title': 'C++', 'content': 'C++ ( pronounced "C plus plus" and sometimes abbreviated as CPP) is a high-level, general-purpose programming language created by Danish computer scientist Bjarne Stroustrup. First released in 1985 as an extension of the C programming language, it has since expanded significantly over time; as of 1997, C++ has object-oriented, generic, and functional features, in addition to facilities for low-level memory manipulation for systems like microcomputers or to make operating systems like Linux or Windows. It is usually implemented as a compiled language, and many vendors provide C++ compilers, including the Free Software Foundation, LLVM, Microsoft, Intel, Embarcadero, Oracle, and IBM.', 'is_published': True},
    {'id': 2, 'title': 'C#', 'content': 'Info about C#', 'is_published': True},
    {'id': 3, 'title': 'Python', 'content': 'Info about Python', 'is_published': False},
    {'id': 4, 'title': 'Java', 'content': 'Info about Java', 'is_published': False},
    {'id': 5, 'title': 'C', 'content': 'Info about C', 'is_published': True},
    {'id': 6, 'title': 'RUST', 'content': 'Info about Rust', 'is_published': False},
    {'id': 7, 'title': 'Golang', 'content': 'Info about Golang', 'is_published': True},
]

categories_db = [
    {'id': 1, 'name': 'Artificial Intelligence'},
    {'id': 2, 'name': 'Machine Learning'},
    {'id': 3, 'name': 'Machine Languages'},
    {'id': 4, 'name': 'Programming Languages'},
]

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

# Create your views here.
def index(request):
    return render(request, "main/index.html", {"title": 'Main Page'})

def test1(request):
    #t = render_to_string('main/index.html')
    data = {'title': 'Test1',
            'menu': menu,
            'float': 28.56,
            'lst': [1,2,'abc', True],
            'set': {1, 2, 3, 4, 5},
            'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
            'obj': MyClass(10,20),
            'category_selected': 0,
            }
    return render(request, 'main/index.html', context=data)

def test2(request):
    data = {'title': 'Main Page',
            'menu': menu,
            'posts': data_db,
            }
    return render(request, 'main/index.html', context=data)

def about(request):
    data = {'title': 'About', 'menu': menu}
    return render(request, 'main/layout.html', context=data)

def add_article(request):
    data = {'title': 'Add Article', 'menu': menu}
    return render(request, 'main/layout.html', context=data)

def contact(request):
    data = {'title': 'Contacts', 'menu': menu}
    return render(request, 'main/layout.html', context=data)

def login(request):
    data = {'title': 'Login', 'menu': menu}
    return render(request, 'main/layout.html', context=data)

def categories(request, category_id):
    return HttpResponse(f"<h1> Categories </h1> <p>id: {category_id}</p>")

def categories_by_slug(request, category_slug):
    return HttpResponse(f"<h1> Categories </h1> <p>slug: {category_slug}</p>")

def language(request, language_slug):
    return HttpResponse(f"<h1> Language </h1> <p>{language_slug}</p>")

def archive(request, year):
    if year > 2024:
        uri = reverse('categories_by_slug', args=('games', ))
        return redirect(uri)
    return HttpResponse(f"<h1> Archive </h1> <p>year: {year}</p>")

def show_category(request, category_id):
    data = {'title': 'Rubrics',
            'menu': menu,
            'posts': data_db,
            'category_selected': category_id,
            }
    return render(request, 'main/index.html', context=data)
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1> Page Not Found! </h1>")