import worker
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=10)
def timed_job():
    os.system('python worker.py')

sched.start()
