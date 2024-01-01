1.项目名称MyBooks,books应用
2.三个模型字段
3. Web 页面，导入数据
eg:
上传书籍文件数据入口:
未选择文件 
月度报告下载入口: 下载

书城列表
title	author	publication date
title 0	author 0	Dec. 20, 2023, 2:58 p.m.
4.
使用celery启动服务，每31天更新一次月度报告，生成路径E:\desktop
celery -A BookStore  worker -l debug -P eventlet
celery -A BookStore beat -l debug 
# 启动python3 manage.py runserver  