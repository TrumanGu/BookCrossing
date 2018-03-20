
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from books.views import *
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', Index.as_view()),
    url('^index/', Index.as_view(), name='index-view'),
    url('^books/', include('books.urls')),
    url('^user/', include('books.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
