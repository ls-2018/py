#!/usr/bin/env python
"""
protobuf
grpcio
"""
import grpc
import time
from concurrent import futures
from proto import hello_pb2, hello_pb2_grpc

GRPC_LISTEN_ADDR = "0.0.0.0:8990"
GRPC_SERVER_SLEEP_SECONDS = 60 * 60 * 24
GRPC_THREAD_POOLS_MAX_WORKERS = 1024


class Hello(hello_pb2_grpc.HelloServicer):
    def hello_action(self, request, context):
        data = request.action
        ip = context.peer()
        print(data, ip)
        reply = hello_pb2.HelloResponse(message=data)
        return reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=GRPC_THREAD_POOLS_MAX_WORKERS))
    hello_pb2_grpc.add_HelloServicer_to_server(Hello(), server)
    server.add_insecure_port(GRPC_LISTEN_ADDR)
    server.start()
    try:
        while True:
            time.sleep(GRPC_SERVER_SLEEP_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
