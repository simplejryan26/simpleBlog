from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myblog.urls')),
    path('members/', include('django.contrib.auth.urls')), #authentication url
    path('members/', include('members.urls')), #members url
]
