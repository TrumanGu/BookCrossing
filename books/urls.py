# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 23:03
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from books.views import *
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'books'

urlpatterns = [
    url(r'^$', BookList, name='book-view'),
    url(r'^list-(?P<type_id>\d+)', BookList, name='list-view'),
    url(r'^detail/(?P<nid>\d+)', BookDetail, name='detail-view'),
    url(r'^register/', register, name='register'),
    url(r'search/', search, name='search'),
    url(r'^user_info/', user_info, name='user-view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)