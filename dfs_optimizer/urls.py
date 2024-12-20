# dfs_optimizer/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('optimizer.urls')),  # Make sure this points to your app's URLs
]
