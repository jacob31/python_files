#!/usr/bin/python
import time

class NotIntegerError(ValueError): pass


class MakeScheduler():

    def set_work_hours(self, work_hours=1):
        ''' sets the number of hours you plan on working 
            defaults to 8 hours.
        '''
        self.work_hours = work_hours
        if int(work_hours) != work_hours:
            raise NotIntegerError('non-integers can not be converted')
        
    
    def set_work_interval(self, work_interval=5):
        ''' max work interval with out a break is 50 minutes.
            defaults to 50 minutes.  Minimum of 5 -10 minute break
            helps keep you eyes healthy.
        '''
        self.work_interval = work_interval
        if int(work_interval) != work_interval:
                raise NotIntegerError('non-integers can not be converted')
        

    def set_break_interval(self, break_interval=1):
        ''' break interval is to remind you to look away from your computer
            This helps protect your eyes.
            default is 10 minutes
        '''
        self.break_interval = break_interval
        if int(break_interval) != break_interval:
                raise NotIntegerError('non-integers can not be converted')
        


    # intervals are based off seconds 50min. == 3000sec.
    def work_hour(work_interval, break_interval):
        intervals = [to_seconds(work_interval), to_seconds(break_interval)]
        print("Starting interval timer...")
        for interval in intervals:
            timer(interval)  # requires seconds
            if interval == work_interval:
                print("Take a break!\a")
            elif interval == break_interval:
                print("Time is up! Back to work...\a")
            else:
                print('error!!!')

    def timer(seconds):
        timer_count = 0
        while timer_count < seconds:
            time.sleep(1)
            timer_count += 1
        pass

    def to_seconds(min):
        return min * 1

    def make_scheduler():
        def scheduler():
            for i in range(work_hours):
                work_hour(work_interval, break_interval)
            pass
        return scheduler


# work_hours = 1
# work_interval = 10
# break_interval = 2

# my_schedule = make_scheduler(work_hours, work_interval, break_interval)

# my_schedule()
