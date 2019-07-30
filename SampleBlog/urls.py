from django.contrib import admin
from . import models, views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name = "index"),
    path('home',views.home, name= 'home'),
    path('blog', views.blog, name = 'blog'),
    path('register', views.register , name = 'register'),
    path('^activate/(?p<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}''-[0-9A-Za-z]{1,20}))/$', views.activate, name = 'activate')
]