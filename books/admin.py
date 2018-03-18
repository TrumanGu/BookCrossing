from django.contrib import admin
from books.models import UserInfo, Category, Goods
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Category)
admin.site.register(Goods)