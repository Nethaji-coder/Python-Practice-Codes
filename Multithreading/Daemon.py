import threading
import time

def background_task():
    while True:
        print('Background task running...')
        time.sleep(1)

thread = threading.Thread(target=background_task)
thread.daemon = True
thread.start()

time.sleep(2)
print("Main thread is Dead.")