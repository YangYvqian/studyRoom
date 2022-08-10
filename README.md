##### 自习室管理系统
###### 命令
- 启动服务 
  python manage.py runserver 0:0:0:0 8080
- 启动项目

- models模型字段修改更新
    - python manage.py migrate
    - python manage.py makemigrations seatManage  # 让 Django 知道我们在我们的模型有一些变更
    - python manage.py migrate seatManage   # 创建表结构
    - python manage.py sqlmigrate seatManage 0001
  
