
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from books.views import *
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', Index.as_view()),
    path('index/', Index.as_view(), name='index-view'),
    path('books/', include('books.urls'), name='goods-view'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
