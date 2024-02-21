from datetime import *
day1 = datetime.now()
day2 = datetime(2024, 1, 12)
difference = day1 - day2
print(difference.total_seconds())
