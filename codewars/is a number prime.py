import math
def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0 and num != 2:
        return False
    if num % 3 == 0 and num != 3:
        return False
    for i in range(3,int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True