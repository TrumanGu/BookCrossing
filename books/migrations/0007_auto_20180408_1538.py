# Generated by Django 2.0.4 on 2018-04-08 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20180327_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_stars',
            field=models.FloatField(default=0, null=True, verbose_name='漂流成功次数'),
        ),
    ]
