import math 
complex_1 = map ( int,input().split(",",1))
distant = next(complex_1) 
times = next(complex_1)

if distant <= 3:
    fee = 13 + times
elif distant > 3 and distant <= 15:
    fee = (distant-3)*2.3+13 + times
elif distant >15:
    fee = (distant-15)*3.45 + 40.6 + times

print("{0:.0f}".format(fee))


