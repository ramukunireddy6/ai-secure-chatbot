from prometheus_client import Counter,start_http_server

BLOCKED = Counter(
    "guardrails_blocked_requests_total",
    "Blocked AI requests",
    ["mitre_tactic"]
)

def init_metrics():
    start_http_server(8001)

def record_block(tactic):
    BLOCKED.labels(metric_tactic=tactic).inc()