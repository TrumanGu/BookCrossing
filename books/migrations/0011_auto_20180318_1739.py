# Generated by Django 2.0.1 on 2018-03-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20180318_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='good_img',
            field=models.ImageField(upload_to='media/upload_imgs'),
        ),
    ]
