# Generated by Django 3.2.14 on 2022-08-09 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seatManage', '0011_alter_userinfo_stop_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='stop_flag',
            field=models.IntegerField(default=0, verbose_name='暂停标志'),
        ),
    ]
