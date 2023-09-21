import unittest
from unittest.mock import patch, MagicMock
import datetime

# Assuming the module name is 'timer_module' and it's in the same directory
from timer_module import count

class TestCount(unittest.TestCase):

    @patch('timer_module.timer_running', True)
    @patch('timer_module.timer_counter_num', 66600)
    @patch('timer_module.label')
    def test_count_time_up(self, mock_label):
        count()
        mock_label.config.assert_called_once_with(text="Time Is Up")
        self.assertEqual(False, timer_running)

    @patch('timer_module.timer_running', True)
    @patch('timer_module.timer_counter_num', 3600)
    @patch('timer_module.label')
    def test_count_time_format(self, mock_label):
        count()
        mock_label.config.assert_called_once_with(text="00:59:59")
        self.assertEqual(3599, timer_counter_num)

    @patch('timer_module.timer_running', False)
    @patch('timer_module.timer_counter_num', 66600)
    @patch('timer_module.label')
    def test_count_not_running(self, mock_label):
        count()
        mock_label.config.assert_not_called()
        self.assertEqual(66600, timer_counter_num)

if __name__ == '__main__':
    unittest.main()
