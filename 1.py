n = int(input())
if n % 8 == 0:
    p = n // 8
    et = 8
else:
    p = n // 8 + 1
    et = n % 8
print(et, p)