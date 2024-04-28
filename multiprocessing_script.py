import multiprocessing
import time
from datetime import datetime
import random
def worker():
    time.sleep(random.random())
    print('Current Time:', datetime.now())
def main():
    processes = [multiprocessing.Process(target=worker) for _ in range(3)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
if __name__ == '__main__':
    main()
