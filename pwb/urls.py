"""pwb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include
from django.views.i18n import set_language

from sp.views import dashboard as dashboard_views

urlpatterns = [
    url(r'^$', dashboard_views.dashboard, name='dashboard'),
    url(r'^admin/', admin.site.urls),
    # url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^setlang/', set_language, name='setlang'),
]

urlpatterns += i18n_patterns(
    url(r'^sp/', include(('sp.urls', 'sp'), namespace='sp')),
)
