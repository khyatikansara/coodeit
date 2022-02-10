from django.urls import path
from portfolio_app import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "portfolio_app"

urlpatterns = [
	path('', views.home, name="home"),
	]