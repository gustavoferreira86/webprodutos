"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from produtos.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('produtos.views',
url(r'^$', 'home', name='home'),
url(r'^cadastro/$', CriarProduto.as_view(), name='cadastro'),
url(r'^cadastroFornecedor/$', CriarFornecedor.as_view(), name='cadastroFornecedor'),
url(r'^cadastroCategoria/$', CriarCategoria.as_view(), name='cadastroCategoria'),
url(r'^lista/$', Lista.as_view(), name='lista'),
url(r'^admin/', include(admin.site.urls)),
url(r'^editar/$', objDetails), 
)
