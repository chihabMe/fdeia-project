
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls',namespace='post') ),
    path('accounts/', include('accounts.urls',namespace='accounts') ),
]

if settings.DEBUG:
    urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
