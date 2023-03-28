from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('wayback_app/', include('wayback_app.urls')),
]
