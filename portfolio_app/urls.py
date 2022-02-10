from . import views
from django.urls import path
from django.conf.urls import patterns, include, url


urlpatterns = [
    url(r'^home/', 'portfolio_app.views.home', name = 'home'),
]
