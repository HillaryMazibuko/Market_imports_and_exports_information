from django.urls import path
from . import views


urlpatterns =[
    path('',views.HomePage,name='HomePage'),
    path('Vane/',views.exports,name='exports'),
    path('Imports/',views.imports,name='imports'),
    path('Vane/Results/',views.Results,name='Results'),
    path('news/',views.news,name='news'),
    path('Vane/sign_in/',views.sign_in,name='sign_in'),
    path('Vane/sign_up/',views.sign_up,name='sign_up'),
    path('search/',views.search_page,name='search'),
    path('table/',views.table,name='table'),
]