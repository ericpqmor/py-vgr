import math
import random

n = input() # Polygon size
r = 100 # Radius

color_array = [('255','0','0'),('0','255','0'),('0','0','255'),('255','0','0'),('255','255','0'),('255','0','255'),('0','255','255'),('0','0','0')]

output_file = open(str(n) + '.txt', 'w+')

for i in range(n):
    output_file.write(str(r * math.cos(2 * math.pi * i/n)) + ',' + str(r * math.sin (2 * math.pi * i/n)) + '\n')

color = random.choice(color_array)
output_file.write(','.join(color) + '\n')