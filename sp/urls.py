from django.conf.urls import url

from sp.views import intro as intro_views

urlpatterns = [
    url(r'^$', intro_views.intro_view, name='dashboard'),
]
