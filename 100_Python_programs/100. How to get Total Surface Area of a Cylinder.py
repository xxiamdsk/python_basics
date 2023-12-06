from math import pi

h = float(input("Insert height of cylinder: "))
r = float(input("Insert radius of cylinder: "))

circles = 2*(pi*r**2)
side = 2*pi*r*h
Area = circles+side

print("Total surface area  = ",round(Area,2))