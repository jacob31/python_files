import clock_in
import unittest

class ScheduleErrors(unittest.TestCase):

    def test_set_work_hours_not_integer(self):
        ''' __set_work_hours should fail when not given an integer '''
        self.assertRaises(clock_in.NotIntegerError, clock_in.MakeScheduler.set_work_hours, 1.5) 

    def test_set_work_interval_not_integer(self):
        ''' __set_work_interval should fail when not given an integer '''
        self.assertRaises(clock_in.NotIntegerError, clock_in.MakeScheduler.set_work_interval, 1.5)

    def test_set_break_interval_not_integer(self):
        ''' __set_break_interval should fail when not given an integer '''
        self.assertRaises(clock_in.NotIntegerError, clock_in.MakeScheduler.set_break_interval, 1.5)





if __name__ == '__main__':
    unittest.main()