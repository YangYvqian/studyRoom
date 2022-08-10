# Generated by Django 2.2.5 on 2022-07-17 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, verbose_name='用户姓名')),
                ('user_phone', models.IntegerField(verbose_name='电话')),
                ('user_sex', models.CharField(max_length=2, verbose_name='用户性别')),
                ('user_fingerprint', models.CharField(max_length=30, verbose_name='用户指纹信息')),
                ('user_card_class', models.CharField(max_length=10, verbose_name='卡种类')),
                ('user_card_number', models.CharField(max_length=15, verbose_name='卡号')),
                ('card_create_time', models.DateField(verbose_name='开卡日期')),
                ('card_expiration_time', models.DateField(verbose_name='卡过期日期')),
                ('modified_time', models.DateField(verbose_name='修改操作时间')),
                ('info_change_time', models.DateField(verbose_name='更改信息时间')),
                ('active_day', models.IntegerField(verbose_name='活跃天数')),
                ('stop_time', models.DateField(verbose_name='暂停时间')),
                ('stop_number', models.DateField(verbose_name='暂停次数')),
                ('user_seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seatManage.Seat')),
            ],
        ),
        migrations.CreateModel(
            name='HistorySeat',
            fields=[
                ('h_id', models.AutoField(primary_key=True, serialize=False)),
                ('seat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='seatManage.Seat')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='seatManage.UserInfo')),
            ],
        ),
    ]
