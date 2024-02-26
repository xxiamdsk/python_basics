
from random import randint

row = 6
col = 6
matrix = []

for i in range(row):
    myrow = []
    for j in range(col):
        myrow.append(randint(1, 100))
    matrix.append(myrow)

for row in matrix:
    print(row)