from datetime import date

date1 = (7, 3, 2025)  # (day, month, year)
date2 = (25, 12, 2024)

d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])

days_between = abs((d1 - d2).days)
print("Number of days between:", days_between)
