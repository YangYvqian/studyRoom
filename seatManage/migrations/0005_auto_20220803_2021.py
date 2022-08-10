# Generated by Django 3.2.14 on 2022-08-03 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seatManage', '0004_auto_20220803_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='card_create_time',
            field=models.CharField(max_length=30, verbose_name='开卡日期'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='card_expiration_time',
            field=models.CharField(max_length=30, verbose_name='卡过期日期'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='info_change_time',
            field=models.CharField(max_length=30, verbose_name='更改信息时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='modified_time',
            field=models.CharField(max_length=30, verbose_name='修改操作时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='stop_number',
            field=models.IntegerField(verbose_name='暂停次数'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='stop_time',
            field=models.CharField(max_length=30, verbose_name='暂停时间'),
        ),
    ]