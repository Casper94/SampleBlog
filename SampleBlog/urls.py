from django.contrib import admin
from . import models, views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name = "index"),
    path('home',views.home, name= 'home'),
    path('blog', views.blog, name = 'blog'),
    path('register', views.register , name = 'register'),
    path('notes', views.addNote, name= 'note'),
    path('subject', views.addSubject, name= 'subject'),
    path('level', views.addLevel, name= 'level'),
    path('ajanx/load-subject/', views.load_subject, name='ajax_load_subject')
    # path('^activate/(?p<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}''-[0-9A-Za-z]{1,20}))/$', views.activate, name = 'activate')

]