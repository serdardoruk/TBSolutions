def nearestPowerOfTwo(num):

    power = 0
    n = num
    while n > 1:
        n //= 2
        power += 1

    if abs(num - 2**power) < abs(num - 2**(power - 1)):
        return 2**power
    
    else:
        return 2**(power - 1)



print(nearestPowerOfTwo(10))
print(nearestPowerOfTwo(2))
print(nearestPowerOfTwo(100))

    
