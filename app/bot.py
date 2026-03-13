import time
from prometheus_client import start_http_server, Counter

print("Trading bot service started")

# metric
trade_checks = Counter('trade_checks_total', 'Number of market checks')

# expose metrics on port 8000
start_http_server(8000)

while True:
    print("Checking market signals...")
    trade_checks.inc()
    time.sleep(5)