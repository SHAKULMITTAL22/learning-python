import unittest
import time
from tkinter import Label, Tk, END
from unittest.mock import patch
from datetime import datetime
from pytz import timezone

# Define date and clock as global variables
date, clock = None, None

# Define country_zones as a global variable
country_zones = {"New York": ["EST", timezone('America/New_York')],
                 "London": ["GMT", timezone('Europe/London')],
                 "Beijing": ["CST", timezone('Asia/Shanghai')],
                 "Tokyo": ["JST", timezone('Asia/Tokyo')]}

def digital_clock():
    global date, clock
    count = 1
    date_local = time.strftime("%a %d %b %Y")
    date.config(text=date_local)
    for country_zone in country_zones.keys():
        country_time = datetime.now(country_zones[country_zone][1])
        country_time_fmt = country_time.strftime(f"{country_zones[country_zone][0]}: %I:%M %p (Timezone: %z)")
        clock = Label(digi_clock, font=clock_font, fg=fg_clock, bd=border_width)
        clock.grid(row=count, column=0)
        clock.config(text=country_time_fmt)
        count += 1
    clock.after(1000, digital_clock)

class TestDigitalClock(unittest.TestCase):

    @patch('time.strftime')
    def test_digital_clock_date(self, mock_strftime):
        global date
        mock_strftime.return_value = "Mon 01 Jan 2022"
        date = Label(text="")
        digital_clock()
        self.assertEqual(date.cget("text"), "Mon 01 Jan 2022")

    @patch('time.strftime')
    def test_digital_clock_time(self, mock_strftime):
        global clock
        mock_strftime.return_value = "12:00:00 AM"
        clock = Label(text="")
        digital_clock()
        self.assertEqual(clock.cget("text"), "12:00:00 AM")

    @patch('datetime.datetime.now')
    def test_digital_clock_time_zones(self, mock_datetime_now):
        global clock
        for country_zone in country_zones.keys():
            mock_datetime_now.return_value = datetime(2022, 1, 1, 0, 0, 0, tzinfo=country_zones[country_zone][1])
            clock = Label(text="")
            digital_clock()
            expected_time = f"{country_zones[country_zone][0]}: 12:00 AM (Timezone: {country_zones[country_zone][1].strftime('%z')})"
            self.assertEqual(clock.cget("text"), expected_time)

if __name__ == '__main__':
    unittest.main()
