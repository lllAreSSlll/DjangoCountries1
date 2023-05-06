from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import json

author = {
    "name": "Рустам",
    "surname": "Садыков",
    "phone": "88005553535",
    "email": "emailsample@sample.org",
}
# items = [
#     {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
#     {"id": 2, "name": "Куртка кожаная", "quantity": 2},
#     {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
#     {"id": 7, "name": "Картофель фри", "quantity": 0},
#     {"id": 8, "name": "Кепка", "quantity": 124},
# ]


# Create your views here.
def home(request):
    context = {
        "name": author['name'],
        "surname": author['surname']
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'author': author
    }
    return render(request, 'about.html', context)


# def item_page(request, id):
#     for item in items:
#         if item['id'] == id:
#             context = {
#                 'item': item
#             }
#             return render(request, 'item-page.html', context)
#
#     return HttpResponseNotFound(f"Товар с id={id} не найден")
#
#
# def items_list(request):
#     # text = "<h2>Список товаров</h2><ol>"
#     # for item in items:
#     #     text += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
#     # text += "</ol>"
#     # return HttpResponse(text)
#     context = {
#         'items': items
#     }
#     return render(request, 'item-list.html', context)

def countries_list(request):
    with open('countries.json') as f:
        countries = json.load(f)
    context = {
        'countries': countries
    }
    return render(request, 'countries_list.html', context)


def country_detail(request, country):
    with open('countries.json', 'r') as f:
        countries = json.load(f)
    country_data = None
    for c in countries:
        if c['country'] == country:
            country_data = c
            break
    context = {'country_data': country_data}
    return render(request, 'country_detail.html', context)


def languages_list(request):
    with open('countries.json', 'r') as f:
        countries = json.load(f)
    languages = []
    for c in countries:
        for l in c['languages']:
            if l not in languages:
                languages.append(l)
    context = {'languages': languages}
    return render(request, 'languages_list.html', context)