from collections import defaultdict
import json
import subprocess
import sys

BENCH = './build/benchmark/uwhpc_benchmark'

if __name__ == '__main__':
    totals = defaultdict(float)
    try:
        count = int(sys.argv[1])
    except Exception:
        count = 10
    for _ in range(count):
        result = subprocess.run([BENCH], capture_output=True, text=True, check=True)
        stats = json.loads(result.stdout)
        for k, v in stats.items():
            totals[k] += v
    for k, v in totals.items():
        totals[k] /= count
    print(dict(totals))