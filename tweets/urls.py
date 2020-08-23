from django.urls import path
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'tweets'

# ここの配列の中にルーティングを書いていきます。
urlpatterns = [
    path('new/', login_required(views.New.as_view()), name='new'),
    path('', login_required(views.Index.as_view()), name='index'),
]