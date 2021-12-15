import redis
from functools import wraps
import time


global redis_client
redis_client = redis.Redis(host = "localhost", port=6379, db = 0)

def cache (function=None):
    @wraps(function)
    def wrapper (*args, **kwargs):
        num = args[0]

        val = redis_client.get(str(num))

        if val:
            print("Data cached")
            return val
        else:
            f = function(*args, **kwargs)
            redis_client.set(str(num), str(f))
            return f

    return wrapper

@cache
def compute(num):
    num = num * num
    time.sleep(4)
    return num * num


if __name__ == "__main__":
    val = compute(9999)
    print(val)