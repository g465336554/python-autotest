import multiprocessing
import os,time

def inputQ (queue):
    info = str(os.getpgid()) + '(put):' + str(time.time())
    queue.put(info)

def outputQ(queue,lock):
    info = queue.get()
    lock.acquire()
    print((str(os.getpgid()) + '(get):' + info))
    lock.release()

if __name__ == '__main__':
    record1 = []
    record2 = []
    lock = multiprocessing.Lock()#加锁，防止散乱的打印
    queue = multiprocessing.Queue(3)
    for i in range (10):
        process = multiprocessing.Process(target=inputQ,args= (queue,))
        process.start()
        record1.append(process)
    for i in range(10):
        process = multiprocessing.Process(target=outputQ,args=(queue,lock))
        process.start()
        record2.append(process)
    for p in record1:
        p.join()
    queue.close()
    for p in record2:
        p.join



