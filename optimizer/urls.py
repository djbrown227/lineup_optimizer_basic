from django.urls import path
from . import views

urlpatterns = [
    path('', views.optimize, name='home'),  # This will handle the root URL
    path('optimize/', views.optimize, name='optimize'),
    path('results/', views.results, name='results'),
    path('download_csv/', views.download_csv, name='download_csv'),  # Ensure this view exists
]
