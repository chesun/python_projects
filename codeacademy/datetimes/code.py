from datetime import datetime

birthday = datetime(1994, 2, 15, 4, 25, 12)
birthday.year  
birthday.second
birthday.weekday()

datetime(2021, 1, 1) - datetime(2001, 12, 28)

# parse a string date-time
parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')

# render a date as a string
date_string = datetime.strftime(datetime.now(), '%A %b %d, %Y')