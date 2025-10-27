from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings

urlpatterns = [
    path('q/', admin.site.urls),
    path('', include('data.urls')),
    path(
        "robots.txt",
        TemplateView.as_view(template_name=f"data/robots.txt", content_type="text/plain"),
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
