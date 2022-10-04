from threading import Thread
class TwinPrime(Thread):
    def __init__(this,a,b):
        Thread.__init__(this)
        this.a, this.b = a, b
    def prime(this,n):
        for i in range(2,n//2+1):
            if(n%i==0):
                return False
        return True
    def run(this):
        if(this.b-this.a==2):
            if (this.prime(this.a) and this.prime(this.b)):
                print("Twin Prime")
                return
        print("Not Twin Prime")   
a=int(input("Enter First number: "))
b=int(input("Enter Second number: "))
TwinPrime(a,b).start()
        
