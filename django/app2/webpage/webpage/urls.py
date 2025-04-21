from django.contrib import admin
from django.urls import path, include  # ✅ make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app3.urls')),
    path('', include('app4.urls')),    # ✅ includes all URLs from app3/urls.py
]
