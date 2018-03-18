# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 23:03
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from books.views import *
from django.conf.urls import url
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('', BookList.as_view(), name='book-view'),
    url(r'list-(?P<type_id>\d+)', BookList.as_view(), name='list-view'),
    url(r'detail-(?P<pk>\d+)', BookDetail.as_view(), name='detail-view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)