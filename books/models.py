from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user_name = models.CharField(max_length=50)
    user_number = models.CharField(max_length=50)
    user_pwd = models.CharField(max_length=50)
    user_stars = models.FloatField(null=True)
    def __str__(self):
        return self.user_name


class Category(models.Model):
    caption = models.CharField(max_length=30)
    def __str__(self):
        return self.caption

class Goods(models.Model):
    good_name = models.CharField(max_length=100)
    good_img = models.ImageField(upload_to='upload_imgs')
    good_context = models.CharField( max_length=300, null=True)
    good_owener = models.ForeignKey(UserInfo, on_delete='CASCADE')
    good_category = models.ForeignKey(Category, on_delete='CASCADE')
    def __str__(self):
        return self.good_name