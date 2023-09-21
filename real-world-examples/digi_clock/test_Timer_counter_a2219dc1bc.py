import unittest
from unittest.mock import MagicMock
import datetime

# Assuming the method is something like this
def timer_counter(label):
    if not isinstance(label, str):
        raise TypeError("Label must be a string.")
    start_time = datetime.datetime.now()
    print(f'{label}: {start_time}')
    return start_time

class TestTimerCounter(unittest.TestCase):
    
    def test_timer_counter_label_type(self):
        with self.assertRaises(TypeError):
            timer_counter(123)

    def test_timer_counter_return_type(self):
        label = "Test"
        self.assertIsInstance(timer_counter(label), datetime.datetime)

if __name__ == '__main__':
    unittest.main()
