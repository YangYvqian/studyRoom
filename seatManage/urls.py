"""studyRoom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.urls import path, include

from . import views
app_name='seatManage'
urlpatterns = [
    path('', views.index),
    path('add_user', views.add_user, name='add_user'),
    path('update_user',views.update_user,name='update_user'),
    path('select_user',views.select_user,name='select_user'),
    path('search',views.search,name='search'),
    path('stop_time', views.stop_time, name='stop_time'),
    path('start_time', views.start_time, name='start_time'),
    path('manage', views.manage, name='manage'),
    path('vail_seat', views.vail_seat, name='vail_seat')

]
