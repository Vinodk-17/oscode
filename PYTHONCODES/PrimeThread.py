#display prime nos using thread, limit given by mainthread
#display fibonaci nos, limit by main thread
from threading import Thread
class primeThread(Thread):
    def __init__(this,limit):
        Thread.__init__(this)
        this.limit = limit
    def run(this):
        print("2")
        for i in range (3,this.limit+1,2):
            flag = True
            for j in range(3,(i//2)+1,2):
                if(i%j==0):
                    flag = False
                    break
            if(flag):
                print(i)

p = primeThread(199999)
p.start()
