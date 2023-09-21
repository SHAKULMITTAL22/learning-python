import unittest
from unittest.mock import Mock, patch
from datetime import datetime
from tkinter import Label
import os

def clock(time_label, date_label):
    date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
    date, time1 = date_time.split()
    time2, time3 = time1.split('/')
    hour, minutes, seconds =  time2.split(':')
    if int(hour) > 11 and int(hour) < 24:
            time = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
    else:
            time = time2 + ' ' + time3
    time_label.config(text = time)
    date_label.config(text= date)
    time_label.after(1000, clock)

class TestClock_23d1af564f(unittest.TestCase):
    def setUp(self):
        self.time_label = Label(text="")
        self.date_label = Label(text="")

    @patch('datetime.datetime.now')
    def test_clock_pm(self, mock_datetime):
        mock_datetime.return_value = datetime(2022, 1, 1, 15, 30, 45) # 3:30:45 PM
        clock(self.time_label, self.date_label)
        self.assertEqual(self.time_label.cget("text"), "3:30:45 PM")
        self.assertEqual(self.date_label.cget("text"), "01-01-2022")

    @patch('datetime.datetime.now')
    def test_clock_am(self, mock_datetime):
        mock_datetime.return_value = datetime(2022, 1, 1, 1, 30, 45) # 1:30:45 AM
        clock(self.time_label, self.date_label)
        self.assertEqual(self.time_label.cget("text"), "1:30:45 AM")
        self.assertEqual(self.date_label.cget("text"), "01-01-2022")
    
    def tearDown(self):
        self.time_label.destroy()
        self.date_label.destroy()

if __name__ == '__main__':
    unittest.main()
