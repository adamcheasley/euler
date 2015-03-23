from datetime import datetime
from dateutil.relativedelta import relativedelta

d = datetime(1901, 1, 1)
sundays_on_the_first = 0

while d.year < 2001:
    if d.weekday() == 6:
        print d.strftime('%Y/%m/%d %A')
        sundays_on_the_first += 1
    d = d + relativedelta(months=1)

print sundays_on_the_first
