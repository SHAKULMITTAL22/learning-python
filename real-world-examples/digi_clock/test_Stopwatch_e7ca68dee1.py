import unittest
from unittest.mock import patch, Mock
from tkinter import *
from tkinter.constants import END

class TestAlarm(unittest.TestCase):

    @patch('tkinter.Entry', autospec=True)
    @patch('tkinter.Label', autospec=True)
    def test_alarm_success(self, mock_label, mock_entry):
        alarm_time = '12:00'
        mock_entry.get.return_value = alarm_time
        alarm_label = mock_label
        alarm_entry = mock_entry
        alarm()
        mock_entry.delete.assert_called_with(0, END)
        mock_label.config.assert_called_with(text='Alarm time: ' + alarm_time)

class TestClock(unittest.TestCase):

    @patch('datetime.datetime.now')
    def test_clock_am(self, mock_datetime):
        mock_datetime.return_value = datetime.datetime(2020, 7, 7, 7, 7, 7)
        self.assertEqual(clock(), '07:07:07 AM')

    @patch('datetime.datetime.now')
    def test_clock_pm(self, mock_datetime):
        mock_datetime.return_value = datetime.datetime(2020, 7, 7, 19, 7, 7)
        self.assertEqual(clock(), '07:07:07 PM')

class TestDigitalClock(unittest.TestCase):

    @patch('tkinter.Label', autospec=True)
    def test_digital_clock_date(self, mock_label):
        digital_clock_label = mock_label
        digital_clock()
        mock_label.config.assert_called()

class TestStopwatch(unittest.TestCase):

    @patch('tkinter.Label', autospec=True)
    @patch('tkinter.Button', autospec=True)
    def test_stopwatch_start(self, mock_button, mock_label):
        stopwatch_label = mock_label
        stopwatch_start = mock_button
        stopwatch('start')
        mock_button.config.assert_called_with(state='disabled')

    @patch('tkinter.Label', autospec=True)
    @patch('tkinter.Button', autospec=True)
    def test_stopwatch_stop(self, mock_button, mock_label):
        stopwatch_label = mock_label
        stopwatch_stop = mock_button
        stopwatch('stop')
        mock_button.config.assert_called_with(state='normal')

    @patch('tkinter.Label', autospec=True)
    @patch('tkinter.Button', autospec=True)
    def test_stopwatch_reset(self, mock_button, mock_label):
        stopwatch_label = mock_label
        stopwatch_reset = mock_button
        stopwatch('reset')
        mock_button.config.assert_called_with(state='normal')

if __name__ == '__main__':
    unittest.main()
