import time
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Seat, UserInfo

HOST = 'http://localhost:8080'

def index(request):
    seat_list = Seat.objects.values('seat_number', 'img_seat_url')
    user = UserInfo.objects.values('id', 'username', 'user_card_class', 'card_create_time', 'user_card_number',
                                   'card_expiration_time', 'user_seat_id', 'stop_flag', 'stop_time', 'flag').filter(
        flag=1)
    seat_list = list(seat_list)
    # 获取当前的时间戳
    curr_time = int(time.time())
    # print(curr_time)
    # 卡是否过期，是flag=0，否，计算剩余多少天
    for user_info in user:
        if user_info.get('card_expiration_time') < curr_time:
            user_info.update({'flag': 0})
            UserInfo.objects.filter(pk=user_info.get('id')).update(flag=0)
        else:
            UserInfo.objects.filter(pk=user_info.get('id')).update(flag=1)
            exp_time = user_info.get('card_expiration_time') - curr_time
            # print(user_info.get('stop_flag'))
            if user_info.get('stop_flag') == 0:
                use_time = curr_time - user_info.get('card_create_time')
                # 获取卡还剩多少天
                rest_day = (exp_time - use_time) // 86400
            elif user_info.get('stop_flag') == 1:
                # print("###")
                stop_time_ = user_info.get('stop_time')
                # print(stop_time_)
                rest_day = (user_info.get('card_expiration_time') - stop_time_) // 86400
            user_info['rest_day'] = rest_day + 1

    for seat_dic in seat_list:
        for user_info in user:
            if seat_dic.get('seat_number') == user_info.get('user_seat_id'):
                seat_dic.update(user_info)
    # print(seat_list)

    return render(request, 'seatManage/index.html', locals())


def add_user(request):
    # ctx = {}
    card_expiration_time = None
    if request.POST:
        user = request.POST
        # print(user)
        card_create_time = int(time.time())
        if user['cardClass'] == '日卡':
            card_expiration_time = (card_create_time + 86400 * 1)
        elif user['cardClass'] == '周卡':
            card_expiration_time = (card_create_time + 86400 * 7)
        elif user['cardClass'] == '月卡':
            card_expiration_time = (card_create_time + 86400 * 31)
        elif user['cardClass'] == '季卡':
            card_expiration_time = (card_create_time + 86400 * 31 * 3)
        elif user['cardClass'] == '半年卡':
            card_expiration_time = (card_create_time + 86400 * 186)
        # print(user)
        user_card_number = int(time.time())
        user_info = UserInfo.objects.create(username=user['username'], user_phone=user['phone'], user_sex=user['sex'],
                                            user_fingerprint=user['fingerPrint'], user_card_class=user['cardClass'],
                                            card_create_time=str(card_create_time), stop_number=0,
                                            card_expiration_time=str(card_expiration_time),
                                            user_card_number=user_card_number,
                                            modified_time=card_create_time, info_change_time=card_create_time,
                                            user_seat_id=user['seat'], flag=1)

    # print(user_info)
    return redirect(HOST+"/seatManage/")


def update_user(request):
    if request.POST:
        user = request.POST

        exp_time = user['date']
        exp_time = int(time.mktime(time.strptime(exp_time[: -1].replace("T", " "), '%Y-%m-%d %H:%M')))
        modified_time = int(time.time())
        info_change_time = int(time.time())
        UserInfo.objects.filter(user_card_number=user['cardNum']).update(user_seat_id=user['updateSeat'],
                                                                         card_expiration_time=exp_time,
                                                                         modified_time=modified_time,
                                                                         info_change_time=info_change_time)
    return redirect(HOST+"/seatManage/")


def timeOf(ts, parttern="%Y-%m-%d %H:%M:%S"):
    try:
        timeArray = time.localtime(int(ts))
        return time.strftime(parttern, timeArray)
    except:
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(ts)))


def select_user(request):
    users = UserInfo.objects.values('id', 'username', 'user_sex', 'user_seat_id', 'user_fingerprint',
                                    'user_card_number',
                                    'user_card_class', 'user_phone', 'card_create_time', 'card_expiration_time',
                                    'modified_time', 'stop_number', 'stop_time', 'flag','stop_flag')
    users = list(users)
    for user_info in users:
        card_create_time = timeOf(user_info.get('card_create_time'))
        card_expiration_time = timeOf(user_info.get('card_expiration_time'))
        modified_time = timeOf(user_info.get('modified_time'))
        if user_info.get('stop_time'):
            stop_time = timeOf(user_info.get('stop_time'))
        else:
            stop_time = 0
        user_info.update({'card_create_time': card_create_time})
        user_info.update({'card_expiration_time': card_expiration_time})
        user_info.update({'modified_time': modified_time})
        user_info.update({'stop_time': stop_time})
        if user_info.get('flag') == 1:
            user_info.update({'flag': '卡正常'})
        else:
            user_info.update({'flag': '卡过期'})
        if user_info.get('stop_flag') == 1:
            user_info.update({'stop_flag': '卡暂停'})
        else:
            user_info.update({'stop_flag': '卡正常'})

    return render(request, 'seatManage/userinfo.html', locals())


def search(request):
    if request.POST:
        user = request.POST
        user = UserInfo.objects.values('id', 'username', 'user_sex', 'user_seat_id', 'user_fingerprint',
                                        'user_card_number',
                                        'user_card_class', 'user_phone', 'card_create_time', 'card_expiration_time',
                                        'modified_time', 'stop_number', 'stop_time', 'flag','stop_flag').filter(user_card_number=user['cardNum'])
        for user_info in user:
            card_create_time = timeOf(user_info.get('card_create_time'))
            card_expiration_time = timeOf(user_info.get('card_expiration_time'))
            modified_time = timeOf(user_info.get('modified_time'))
            if user_info.get('stop_time'):
                stop_time = timeOf(user_info.get('stop_time'))
            else:
                stop_time = 0
            user_info.update({'card_create_time': card_create_time})
            user_info.update({'card_expiration_time': card_expiration_time})
            user_info.update({'modified_time': modified_time})
            user_info.update({'stop_time': stop_time})
            if user_info.get('flag') == 1:
                user_info.update({'flag': '卡正常'})
            else:
                user_info.update({'flag': '卡过期'})
            if user_info.get('stop_flag') == 1:
                user_info.update({'stop_flag': '卡暂停'})
            else:
                user_info.update({'stop_flag': '卡正常'})



    return render(request, 'seatManage/search.html', locals())


def stop_time(request):
    if request.POST:
        time_stop_info = request.POST
        modified_time = int(time.time())
        time_stop = time_stop_info['zDate']
        time_stop = int(time.mktime(time.strptime(time_stop[: -1].replace("T", " "), '%Y-%m-%d %H:%M')))
        # print(time_stop)
        stop_num = UserInfo.objects.values('stop_number').filter(user_card_number=time_stop_info['cNum'])
        stop_number = stop_num[0].get('stop_number') + 1
        UserInfo.objects.filter(user_card_number=time_stop_info['cNum']).update(modified_time=modified_time,
                                                                                stop_number=stop_number,
                                                                                stop_time=time_stop,
                                                                                stop_flag=1)
    return redirect(HOST+"/seatManage/manage")


def timestamp_to_time(ts):
    try:
        return int(time.mktime(time.strptime(ts[: -1].replace("T", " "), '%Y-%m-%d %H:%M')))
    except:
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(ts)))


def manage(request):
    users = UserInfo.objects.values('id', 'username', 'user_sex', 'user_seat_id', 'user_fingerprint',
                                    'user_card_number',
                                    'user_card_class', 'user_phone', 'card_create_time', 'card_expiration_time',
                                    'modified_time', 'stop_number', 'stop_time', 'flag','stop_flag').filter(stop_flag=1)
    users = list(users)
    for user_info in users:
        card_create_time = timeOf(user_info.get('card_create_time'))
        card_expiration_time = timeOf(user_info.get('card_expiration_time'))
        modified_time = timeOf(user_info.get('modified_time'))
        if user_info.get('stop_time'):
            stop_time = timeOf(user_info.get('stop_time'))
        else:
            stop_time = 0
        user_info.update({'card_create_time': card_create_time})
        user_info.update({'card_expiration_time': card_expiration_time})
        user_info.update({'modified_time': modified_time})
        user_info.update({'stop_time': stop_time})
        if user_info.get('flag') == 1:
            user_info.update({'flag': '卡未过期'})
        else:
            user_info.update({'flag': '卡过期'})
        if user_info.get('stop_flag') == 1:
            user_info.update({'stop_flag': '卡暂停'})
        else:
            user_info.update({'stop_flag': '卡正常'})

    return render(request, 'seatManage/manage.html', locals())


def start_time(request):
    if request.POST:
        time_start_info = request.POST
        modified_time = int(time.time())
        cur = int(time.time())
        user = UserInfo.objects.values('user_card_number', 'card_expiration_time', 'stop_time', 'stop_flag').filter(
            user_card_number=time_start_info['sNum'])
        if user[0].get('stop_flag') == 1:
            card_expiration_time = cur + user[0].get('card_expiration_time') - user[0].get('stop_time')
            # print(card_expiration_time)
            UserInfo.objects.filter(user_card_number=time_start_info['sNum']).update(
                card_expiration_time=card_expiration_time, stop_flag=0)

    return redirect(HOST+"/seatManage/manage")


def vail_seat(request):
    if request.POST:
        seat = request.POST['updateSeat'].strip()
        # print(seat)
        if UserInfo.objects.filter(user_seat_id=seat):
            return HttpResponse('1')
        else:
            return HttpResponse('0')
    return render(request,'seatManage/index.html',locals())