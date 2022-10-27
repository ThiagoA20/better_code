# from datetime import datetime
import time

def withoutGenerators():
    start_time = time.time()
    for i in range(100000):
        print(i)
    end_time = time.time()
    return end_time - start_time

def withGenerators():
    start_time = time.time()

    end_time = time.time()
    return end_time - start_time

