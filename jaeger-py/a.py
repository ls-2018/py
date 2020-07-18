import requests
import time
from opentracing_instrumentation.client_hooks import install_all_patches
from jaeger_client import Config

config = Config(config={'sampler': {'type': 'const', 'param': 1},
                        'logging': True,
                        'local_agent': {'reporting_host': '127.0.0.1'}},
                service_name="jaeger_opentracing_example")
tracer = config.initialize_tracer()
# Automatically trace all requests made with 'requests' library.
install_all_patches()

requests.get("http://127.0.0.1:5000/")

time.sleep(2)
tracer.close()
