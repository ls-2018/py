# pip install locustio==0.8a2
import random
from locust import HttpUser, between, TaskSet, task, tag


class MyTaskSet(TaskSet):
    last_wait_time = 0

    @task(2)
    def index(self):
        with self.client.get("/", catch_response=True) as response:
            if response.content != "123":
                response.failure("Got wrong response")

    @tag('tag1', 'tag2')  # 可以使用--tags和--exclude-tags参数对测试期间执行的任务保持谨慎
    @task(1)
    def index2(self):
        self.client.get("/index")

    def wait_time(self):
        self.last_wait_time += 1
        return self.last_wait_time


class WebsiteUser(HttpUser):
    wait_time = between(1, 2)  # 模拟用户在每次执行任务后等待介于最小值和最大值之间的随机时间。
    tasks = [MyTaskSet]
    weight = 1  # Web用户的权重是3
    host = 'http://127.0.0.1:5000'  # 请求的url
    # def on_start(self):
    #     """ 每一次请求时调用 """
    #     print('start')
    #
    # def on_stop(self):
    #     print('end')
# locust --web-host=http://127.0.0.1:8090
