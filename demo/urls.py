from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import home, estatic, view_csv, view_json

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('estatico/', estatic, name='static'),
    path('csv/', view_csv, name='csv'),
    path('json/', view_json, name='json'),
    path('i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
