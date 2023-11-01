from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import *
from account.views import profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('account/profile/', profile, name='profile'),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

