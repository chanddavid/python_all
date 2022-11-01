import threading
import time
import logging

def myfunc():
    logging.info("this is sub trd 1")
    time.sleep(2)
    logging.info("this is sub trd 2")
    

if __name__=="__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads=[]
    for i in range(3):
        logging.info("This is main 1")
        trd=threading.Thread(target=myfunc)
        threads.append(trd)
        trd.start()
    

    for j,k in enumerate(threads):
        logging.info("i am inner ")
        k.join()
        logging.info("i am outer ")