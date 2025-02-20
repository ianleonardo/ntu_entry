import math

def check_divisibility(num, divisor):
    try:
        if(math.fmod(num, divisor) == 0):
            return True
        else:
            return False
    except:
        return False


print(check_divisibility(10, 2))
print(check_divisibility(7, 3))