# optimizer/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.optimize, name='optimize'),  # Handle the root URL
    path('results/', views.results, name='results'),  # Results page URL
]
