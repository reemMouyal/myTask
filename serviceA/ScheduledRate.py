import queue
import time
import schedule
import threading

class ScheduledRate:	
	lock = threading.Lock()
	sumData=0	
	def __init__(self,sizeQ,func):
        # body of the constructor
		self.q = queue.Queue(sizeQ)
		self.func=func
	
	def sampleRate(self):
         with self.lock:
            if self.q.full(): 
               last=self.q.get()  
               self.sumData-=last
            rate=self.func()
            self.sumData+=rate
            self.q.put(rate)   
	
	def calcAVGCoinRete(self):
         if self.sumData==0:
             return self.func()  
         return  self.sumData/self.q.qsize()
		 
	def scheule_a_job(self,sec):
		schedule.every(sec).seconds.do(self.sampleRate)
		while True:
            # Checks whether a scheduled task 
            # is pending to run or not
			schedule.run_pending()
			time.sleep(1)

