# Generated by Django 2.0.1 on 2018-03-27 15:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20180327_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='good_owener',
            field=models.ForeignKey(editable=False, on_delete='CASCADE', to=settings.AUTH_USER_MODEL, verbose_name='拥有者'),
        ),
    ]
