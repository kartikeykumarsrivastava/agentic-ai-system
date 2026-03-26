import time

def log_step(name):
    def wrapper(func):
        def inner(state):
            start = time.time()
            print(f"[START] {name}")

            result = func(state)

            print(f"[END] {name} | Time: {time.time() - start:.2f}s")
            return result
        return inner
    return wrapper