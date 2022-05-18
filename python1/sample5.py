x = 3127
y = 8201
i = 0
while x > 0 and y > 0:
    if x > y:
        x %= y
        i = y
    else:
        y %=  x
        i = x
print(i)