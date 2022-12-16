from django.conf.urls import *
from django.urls import re_path, path
from .models import *
from .forms import *
from cvapp2022 import *
from .views import (
    person_create,
    person_edit,
    person_delete,
    degree_create,
    degree_edit,
    degree_delete,       
    degree_list,
)


urlpatterns = [
    re_path(r'^person/create/$',person_create,name='person-create'),
    re_path(r'^person/(?P<pk>\d+)/edit/$',person_edit,name='person-edit'),
    re_path(r'^person/(?P<pk>\d+)/delete/$',person_delete,name='person-delete'),
    re_path(r'^degree/create/$',degree_create,name='degree-create'),
    re_path(r'^degree/(?P<pk>\d+)/edit/$',degree_edit,name='degree-edit'),
    re_path(r'^degree/(?P<pk>\d+)/delete/$',degree_delete,name='degree-delete'),
    re_path(r'^degree/list/$',degree_list,name='degree-list'),
]