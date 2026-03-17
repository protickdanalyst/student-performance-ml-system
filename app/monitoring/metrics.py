REQUEST_COUNT = 0
FAIL_COUNT = 0
LATENCIES = []

def record(latency, success):
    global REQUEST_COUNT, FAIL_COUNT
    REQUEST_COUNT += 1
    if not success:
        FAIL_COUNT += 1
    LATENCIES.append(latency)

def get_metrics():
    return {
        "requests": REQUEST_COUNT,
        "failures": FAIL_COUNT,
        "avg_latency": sum(LATENCIES)/len(LATENCIES) if LATENCIES else 0
    }