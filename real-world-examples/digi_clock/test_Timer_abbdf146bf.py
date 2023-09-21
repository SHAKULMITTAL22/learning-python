import unittest
from unittest.mock import patch, Mock
from tkinter import *
from tkinter.ttk import *

class TestTimer_abbdf146bf(unittest.TestCase):
    @patch('tkinter.Entry.get')
    @patch('tkinter.Button.config')
    @patch('tkinter.Label.config')
    def test_timer_start(self, mock_label_config, mock_button_config, mock_entry_get):
        global timer_running, timer_counter_num
        timer_counter_num = 66600
        mock_entry_get.return_value = '01:30:30'
        timer('start')
        self.assertTrue(timer_running)
        self.assertEqual(timer_counter_num, 66600 + 60 * 60 + 30 * 60 + 30)
        mock_button_config.assert_any_call(state='disabled')
        mock_button_config.assert_any_call(state='enabled')
        mock_label_config.assert_not_called()

    @patch('tkinter.Button.config')
    def test_timer_stop(self, mock_button_config):
        global timer_running
        timer('stop')
        self.assertFalse(timer_running)
        mock_button_config.assert_any_call(state='disabled')
        mock_button_config.assert_any_call(state='enabled')

    @patch('tkinter.Entry.config')
    @patch('tkinter.Button.config')
    @patch('tkinter.Label.config')
    def test_timer_reset(self, mock_label_config, mock_button_config, mock_entry_config):
        global timer_running, timer_counter_num
        timer('reset')
        self.assertFalse(timer_running)
        self.assertEqual(timer_counter_num, 66600)
        mock_button_config.assert_any_call(state='disabled')
        mock_button_config.assert_any_call(state='enabled')
        mock_entry_config.assert_called_once_with(state='enabled')
        mock_label_config.assert_called_once_with(text='Timer')

if __name__ == '__main__':
    unittest.main()
