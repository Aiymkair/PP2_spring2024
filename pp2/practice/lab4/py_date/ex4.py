from datetime import *
day1 = datetime.now()
day2 = datetime(2024, 1, 12)
dif = day1 - day2
print(dif.total_seconds())
