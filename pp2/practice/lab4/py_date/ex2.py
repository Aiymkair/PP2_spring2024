from datetime import *
tomorrow = datetime.today() + timedelta(days=1)
current = datetime.today()
yesterday = current - timedelta(days=1)

print("Yesterday:", yesterday)
print("Current date:", current)
print("Tommorow:", tomorrow)