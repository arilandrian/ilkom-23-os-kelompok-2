import threading
import time

def worker(thread_name):
    print(f'Thread {thread_name}mulai bekerja.')
    time.sleep(2)
    print(F'Thread {thread_name} selesai')

thread1 = threading.Thread(target=worker, args=('A',))
thread2 = threading.Thread(target=worker, args=('B',))

thread1.start()
thread2.start()