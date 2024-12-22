from django.urls import path
from . import views

urlpatterns = [
    path('', views.optimize, name='home'),  # Handles the root URL
    path('optimize/', views.optimize, name='optimize'),  # Use `optimize` view
    path('results/', views.results, name='results'),  # Use `results` view
    path('download_csv/', views.download_csv, name='download_csv'),  # Use `download_csv` view
]
