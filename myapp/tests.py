from django.test import TestCase

# Create your tests here.

# from datetime import date
#
# d0 = date(2020, 4, 1)
# d1 = date(2024, 4, 29)
# delta = d1 - d0
# print(delta.days)


import datetime
today = datetime.date.today()
# print(today)

last_year = datetime.date(2007, 9, 1)
print(today - last_year)
