import multiprocessing

def proc1(pipe):
    pipe.send('hello')
    print('procl rec:', pipe.recv())

def procl2(pipe):
    print('procl2 rec:',pipe.recv())
    pipe.send('hello too')

if __name__ == '__main__':
    multiprocessing.freeze_support()
    pipe= multiprocessing.Pipe()

    p1= multiprocessing.Process(target= proc1,args=(pipe[0],))
    p2 = multiprocessing.Process(target=procl2, args=(pipe[1],))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
