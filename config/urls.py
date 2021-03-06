# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('users/', include('demigos.users.urls')),
    path('', include('demigos.crypto.urls')),
    # Your stuff: custom urls includes go here
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
