f1 = 0
f2 = 1
f3 = 1
s = 0
while f3 < 4000000:
    f3 = f2 + f1 
    f1 = f2 #after finding the number on f3, we need to do the sum of the last 2 numbers, so we sum the numbers on f3 and f2, changing the num f3 to obj. f2 and the same with the num f2 to obj. f1
    f2 = f3
    if f3 % 2 == 0:
        s += f3
print(f'The sum of the even numbers of the Fibonnaci sequence that do not exceed 4Million is {s}')