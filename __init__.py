import os,sys
import schedule
import time
from printing import play

def hell():
    print'Hell_Function is called'
    play()
   


def call():
    schedule.every(0.05).minutes.do(hell)
    while True:
        schedule.run_pending()
        time.sleep(0.05)

if __name__ == '__main__':
    call()
        