import time

from django.db import models


# Create your models here.
class UserInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=30, verbose_name="用户姓名")
    user_phone = models.CharField(max_length=30, verbose_name="电话")
    user_sex = models.CharField(max_length=2, verbose_name="用户性别")
    user_fingerprint = models.CharField(max_length=30, verbose_name="用户指纹信息")
    user_seat = models.ForeignKey("Seat", on_delete=models.CASCADE)
    user_card_class = models.CharField(max_length=10, verbose_name="卡种类")
    user_card_number = models.CharField(max_length=15, verbose_name="卡号",default=0)
    card_create_time = models.BigIntegerField(verbose_name="开卡日期")
    card_expiration_time = models.BigIntegerField(verbose_name="卡过期日期")
    modified_time = models.BigIntegerField(verbose_name="修改操作时间")
    info_change_time = models.BigIntegerField(verbose_name="更改信息时间")
    active_day = models.IntegerField(verbose_name="活跃天数",default=0)
    stop_time = models.BigIntegerField(verbose_name="暂停时间",default=0)
    stop_number = models.IntegerField(verbose_name="暂停次数")
    flag = models.IntegerField(verbose_name="过期标志",default=1)
    stop_flag = models.IntegerField(verbose_name='run暂停标志',default=0)


class Seat(models.Model):
    id = models.BigAutoField(primary_key=True)
    seat_number = models.IntegerField()
    img_seat_url = models.CharField(max_length=90,verbose_name="图片地址")


class HistorySeat(models.Model):
    h_id = models.AutoField(primary_key=True)
    user = models.OneToOneField("UserInfo", on_delete=models.CASCADE)
    seat = models.OneToOneField("seat",on_delete=models.CASCADE)
