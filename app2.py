import math
import random
from datetime import datetime

# Generate a random number
num = random.randint(1, 100)
print(f"Random number: {num}")

# Calculate its square root
sqrt = math.sqrt(num)
print(f"Square root: {sqrt:.2f}")

# Show the current date and time
now = datetime.now()
print("Current time:", now.strftime("%Y-%m-%d %H:%M:%S"))
