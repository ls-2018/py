#!/usr/bin/env python
import grpc
from proto import hello_pb2, hello_pb2_grpc

data = """
{
    "id": 1
}
"""


def run():
    channel = grpc.insecure_channel("localhost:8990")
    stub = hello_pb2_grpc.HelloStub(channel)
    response = stub.hello_action(hello_pb2.HelloRequest(action=data))
    print("Hello result received:  %s" % response.message)


if __name__ == '__main__':
    run()
