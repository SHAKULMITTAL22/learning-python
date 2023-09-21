import unittest
from unittest.mock import patch, Mock
import datetime
import platform
import os

class Alarm:
    def __init__(self):
        self.get_alarm_time_entry = None
        self.alarm_status_label = None
        self.set_alarm_button = None

    def alarm(self):
        main_time = datetime.datetime.now().strftime("%H:%M %p")
        alarm_time = self.get_alarm_time_entry.get()
        alarm_time1,alarm_time2 = alarm_time.split(' ')
        alarm_hour, alarm_minutes = alarm_time1.split(':')
        main_time1,main_time2 = main_time.split(' ')
        main_hour1, main_minutes = main_time1.split(':')
        if main_time2 == 'PM':
            main_hour = str(int(main_hour1) - 12)
        else:
            main_hour = main_hour1
        if int(alarm_hour) == int(main_hour) and int(alarm_minutes) == int(main_minutes) and main_time2 == alarm_time2:
            for i in range(3):
                self.alarm_status_label.config(text='Time Is Up')
                if platform.system() == 'Windows':
                    os.system('beep -f 5000')
                elif platform.system() == 'Darwin':
                    os.system('say Time is Up')
                elif platform.system() == 'Linux':
                    os.system('beep -f 5000')
            self.get_alarm_time_entry.config(state='enabled')
            self.set_alarm_button.config(state='enabled')
            self.get_alarm_time_entry.delete(0,END)
            self.alarm_status_label.config(text = '')
        else:
            self.alarm_status_label.config(text='Alarm Has Started')
            self.get_alarm_time_entry.config(state='disabled')
            self.set_alarm_button.config(state='disabled')
        self.alarm_status_label.after(1000, self.alarm)

class TestAlarm(unittest.TestCase):

    @patch('os.system')
    @patch('datetime.datetime')
    def test_alarm_success(self, mock_datetime, mock_os):
        alarm = Alarm()
        alarm.get_alarm_time_entry = Mock()
        alarm.alarm_status_label = Mock()
        alarm.set_alarm_button = Mock()
        mock_datetime.now.return_value.strftime.return_value = "12:00 AM"
        alarm.get_alarm_time_entry.get.return_value = "12:00 AM"
        alarm.alarm()
        alarm.alarm_status_label.config.assert_called_with(text='Time Is Up')
        mock_os.assert_called_with('beep -f 5000')
        alarm.get_alarm_time_entry.config.assert_called_with(state='enabled')
        alarm.set_alarm_button.config.assert_called_with(state='enabled')

    @patch('os.system')
    @patch('datetime.datetime')
    def test_alarm_failure(self, mock_datetime, mock_os):
        alarm = Alarm()
        alarm.get_alarm_time_entry = Mock()
        alarm.alarm_status_label = Mock()
        alarm.set_alarm_button = Mock()
        mock_datetime.now.return_value.strftime.return_value = "12:00 PM"
        alarm.get_alarm_time_entry.get.return_value = "12:00 AM"
        alarm.alarm()
        alarm.alarm_status_label.config.assert_called_with(text='Alarm Has Started')
        alarm.get_alarm_time_entry.config.assert_called_with(state='disabled')
        alarm.set_alarm_button.config.assert_called_with(state='disabled')

if __name__ == '__main__':
    unittest.main()
