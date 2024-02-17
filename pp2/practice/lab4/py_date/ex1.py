from datetime import *

current = datetime.today()
after5days = current - timedelta(days=5)

print("Current date:", current)
print("Date five days ago:", after5days)
