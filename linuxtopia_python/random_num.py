import random, time
random.seed(time.clock())
# Simple Range 0 <= r < 6
print(random.randrange(6), random.randrange(6))
# More complex range 1 <= r < 7
print(random.randrange(1,7), random.randrange(1,7))
# Really complex range of even numbers between 2 and 36
print(random.randrange(2,37,2))
# Odd numbers from 1 to 35
print(random.randrange(1,36,2))