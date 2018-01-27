from apscheduler.schedulers.blocking import BlockingScheduler
import worker

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=10)
def timed_job():
    print('This job is run every ten minutes.')

sched.start()
