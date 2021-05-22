import time

def timed(fn):
    def wrapped():
        start = time.time()
        fn()
        print("work for ", time.time() - start)
    return wrapped()

@timed
def hello_world():
    time.sleep(0.1)
    print("hello world")

print("start program")
hello_world()
