from django.contrib import admin
from books.models import Category, Goods, User
# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Goods)