# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 22:06
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @File    : forms.py
# @Software: PyCharm

from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "user_number")