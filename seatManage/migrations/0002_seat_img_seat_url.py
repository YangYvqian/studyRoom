# Generated by Django 2.2.5 on 2022-07-17 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seatManage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='img_seat_url',
            field=models.CharField(default=0, max_length=90, verbose_name='图片地址'),
            preserve_default=False,
        ),
    ]
