# Generated by Django 3.2.14 on 2022-08-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seatManage', '0010_alter_seat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='stop_time',
            field=models.BigIntegerField(default=0, verbose_name='暂停时间'),
        ),
    ]