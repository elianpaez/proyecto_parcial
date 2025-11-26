# scraper/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.scrape_view, name='scraper_home'),
]