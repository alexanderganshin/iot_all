import math

spi = [7.713, 0.208, 6.336, 7.488, 4.985, 2.248, 1.981, 7.605, 1.691, 0.883, 6.854, 9.534, 0.039]
sp2 = [7.713, 0.208, 6.336, 7.488, 4.985, 2.248, 1.981, 7.605, 1.691, 0.883, 6.854, 9.534, 0.039]


for i in range(len(sp2)):
    sp2[i] -= int(sp2[i])
print(sp2)

for i in range(len(sp2)-1):
    if sp2[i] < sp2[i+1]:
        max = i+1
print(max)
print(int(spi[max]))