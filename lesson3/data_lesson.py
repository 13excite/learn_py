from datetime import datetime, date, timedelta

print("Today: {}".format(datetime.now().strftime("%Y-%m-%d")))
print("Yesterday was {}".format(date.today() - timedelta(1)))
print("30 days ago was {}".format(date.today() - timedelta(days=30)))

date_string = "01/01/17 12:10:03.234567"
print("Format string {0} to datetime {1}".format(date_string, datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')))