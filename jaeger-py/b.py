import logging
from jaeger_client import Config
from flask_opentracing import FlaskTracing
from flask import Flask, request
from os import getenv

JAEGER_HOST = getenv('JAEGER_HOST', 'localhost')

app = Flask(__name__)
log_level = logging.DEBUG
logging.getLogger('').handlers = []
logging.basicConfig(format='%(asctime)s %(message)s', level=log_level)
config = Config(
    config={
        'sampler': {'type': 'const', 'param': 1},
        'logging': True,
    },
    service_name="jaeger-python"
)
jaeger_tracer = config.initialize_tracer()
# tracing = FlaskTracing(jaeger_tracer) # 只追踪有@tracing.trace()装饰的
tracing = FlaskTracing(jaeger_tracer, True, app, )  # 所有请求都追踪


@app.route('/')
def index():
    with jaeger_tracer.start_span(index)  as span:
        span.set_tag("asd", 12)
        span.log_kv({'event': 'test message', 'life': 42})

        with jaeger_tracer.start_span('ChildSpan', child_of=span) as child_span:
            child_span.log_kv({'event': 'down below'})
    return "log"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
