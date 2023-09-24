from django.conf.urls.static import static
from django.conf import settings

from django.urls import path, include
from django.contrib import admin

import questoes.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('questoes/', include(questoes.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)