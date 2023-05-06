from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    # path('item/<int:id>/', views.item_page),
    # path('items/', views.items_list),
    path('countries-list/', views.countries_list, name='countries_list'),
    path('countries/<str:country>/', views.country_detail, name='country_detail'),
    path('languages/', views.languages_list, name='languages_list'),
]