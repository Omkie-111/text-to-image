from django.urls import path
from .views import image_generation
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('generate-images/', image_generation, name='generate-images'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)