# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 22:06
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @File    : forms.py
# @Software: PyCharm

from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm
from django import forms
from django.forms import widgets as Fwidgets
from django.forms import inlineformset_factory


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "user_number")
#
# class BookForm(form):
#     book_name = forms.CharField(label="书名",max_length=32,required=True)
#     book_img = forms.ImageField(label="图片(必填)",required=True)
#     good_img_2nd = forms.ImageField( label="图片(选填)",required=False)
#     good_img_3rd = forms.ImageField(label="图片(选填)",required=False)
#     good_context = forms.CharField(label="书本详细信息",max_length=300,required=True,widget=forms.Textarea())
#     # good_owener = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"hidden"}))
#     good_category = forms.ModelChoiceField(label='书本分类',queryset=Category.objects.all())

class BookForm(ModelForm):
    class Meta:
        model = Goods
        fields = '__all__'
        # exclude = ('good_owener',)
        # widgets = {
        #     'good_owener':Fwidgets.HiddenInput()
        # }
