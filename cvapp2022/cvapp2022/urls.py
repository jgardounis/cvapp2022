"""cvapp2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path,path
from django.conf.urls import include
from cvapp2022byte.views import (
	index,
	)
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',index,name='cvapp_home'),
    re_path(r'^cvapp2022byte/', include(('cvapp2022byte.urls','cvapp2022byte'))),
]
