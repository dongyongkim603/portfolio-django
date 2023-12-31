from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import conf, path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('page_details.urls', namespace="page_details")),
    path('api/v1/', include('user_details.urls', namespace="user_details")),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('forum.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
