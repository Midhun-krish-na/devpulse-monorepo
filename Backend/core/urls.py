from django.contrib import admin
from django.urls import path, include


urlspattern = [
    path('admin/', admin.site.get_urls()),
    path('api/v1/', include('apps.pulses.urls')),
]