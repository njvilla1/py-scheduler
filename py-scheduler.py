from operator import itemgetter
import time

class WBScheduler():
    
    def __init__(self):
        self.jobs = []
        self.start_time = 0
    
    def add_job(self, period, func, *args, **kwargs):
        self.jobs.append({'func':func, 'args':args, 'kwargs':kwargs, 'period': period, 'count':0, 'next_run':0})

    def start(self):
        self.start_time = time.time()
        while True:
            self.jobs = sorted(self.jobs, key=itemgetter('next_run'))
            time.sleep(max(self.jobs[0]['next_run'] - time.time(), 0))
            self.jobs[0]['func'](*self.jobs[0]['args'], **self.jobs[0]['kwargs'])
            self.jobs[0]['count'] += 1
            self.jobs[0]['next_run'] = max(self.start_time + self.jobs[0]['count']*self.jobs[0]['period'], 0)

if __name__=='__main__':

    def hello(s, test='kwarg'):
        print('hello', test, s, time.time())
        time.sleep(.3)

    sched = WBScheduler()
    sched.add_job(3, hello, 'three', test='asdf')
    sched.add_job(1, hello, 'one')
    sched.start()