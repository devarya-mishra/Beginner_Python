def Is_Armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if sum == num:
        print(f"{num} is Armstronng Number")    

for i in range(1, 1001):
    Is_Armstrong(i)
