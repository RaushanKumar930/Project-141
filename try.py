import json
import numpy as np

salary = np.power(100, 4, dtype=np.int64)

# ⛔️ TypeError: Object of type int64 is not JSON serializable
json_str = json.dumps({'salary': int(salary)})

print(json_str)
