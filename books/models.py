from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    user_number = models.CharField(max_length=50,verbose_name='用户名')
    user_info = models.CharField(max_length=100, null=True, blank=True,verbose_name='联系方式')
    user_stars = models.FloatField(null=True,default=5,verbose_name='用户等级(默认为5)')
    class Meta(AbstractUser.Meta):
        pass


class Category(models.Model):
    caption = models.CharField(max_length=30,verbose_name='分类')
    def __str__(self):
        return self.caption

class Goods(models.Model):
    good_name = models.CharField(max_length=100,verbose_name='书名')
    good_img = models.ImageField(upload_to='upload_imgs',verbose_name='图片')
    good_img_2nd = models.ImageField(upload_to='upload_imgs',null=True,blank=True,verbose_name='图片(可选)')
    good_img_3rd = models.ImageField(upload_to='upload_imgs',null=True,blank=True,verbose_name='图片(可选)')
    good_context = models.CharField( max_length=300, null=True,verbose_name='详细信息')
    good_owener = models.ForeignKey(User, on_delete='CASCADE',verbose_name='拥有者',editable=False)
    good_category = models.ForeignKey(Category, on_delete='CASCADE',verbose_name='分类')
    def __str__(self):
        return self.good_name