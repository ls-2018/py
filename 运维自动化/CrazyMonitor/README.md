# CrazyMonitor
用python写的强大的分布式监控软件 
参考zabbix,openfalcon架构，前端、后端、监控插件、画图、数据优化存储等全部自己实现，通过学习本项目可以了解复杂自动化项目的架构设计、程序解耦原则、前后端数据交互等多项实战技能。


## 启动

    python3 manage.py runserver 0.0.0.0:9000  启动监控服务web端

    python3 MonitorServer.py start  启动监控主程序

    python3 MonitorServer.py trigger_watch  启动报警监听程序

