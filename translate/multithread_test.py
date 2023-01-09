# from google_trans_new import google_translator 
from multiprocessing.dummy import Pool as ThreadPool
import time

pool = ThreadPool(8) # Threads

def request(text):
    print("hello " + text)
    return "hello " + text 

if __name__ == "__main__" :
    time1 = time.time()
    with open("./test.txt",'r') as f_p:
        texts = f_p.readlines()
        try:
            results = pool.map(request, texts)
        except Exception as e:
            raise e
        pool.close()
        pool.join()

        time2 = time.time()
        print("Translating %s sentences, a total of %s s"%(len(texts),time2 - time1))
