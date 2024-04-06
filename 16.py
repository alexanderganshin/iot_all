x = int(input())
y = int(input())

if ((x-1)**2 + y**2) >= 1 and ((x-1)**2 + y**2) <= 4 and (abs(x-4)) <= 2 and (abs(y-2)) <= 3:
    print("yes yes")

if ((x-1)**2 + y**2) >= 1 and ((x-1)**2 + y**2) <= 4 and (abs(x-4)) > 2 and (abs(y-2)) > 3:
    print("yes no")

if ((x-1)**2 + y**2) < 1 and ((x-1)**2 + y**2) > 4 and (abs(x-4)) <= 2 and (abs(y-2)) <= 3:
    print("no yes")

if (((x-1)**2 + y**2) < 1 or ((x-1)**2 + y**2) > 4) and (abs(x-4)) > 2 and (abs(y-2)) > 3:
    print("no no")