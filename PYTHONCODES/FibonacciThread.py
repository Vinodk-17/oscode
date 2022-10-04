from threading import Thread
class fibonacciThread(Thread):
    def __init__(this,limit):
        Thread.__init__(this)
        this.limit = limit
    def run(this):
        a = 0
        b = 1
        while (a<this.limit):
            print(a)
            a,b = b,a+b
fibonacciThread(5000).start()
