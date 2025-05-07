def reverse(x):
    sign = -1 if x < 0 else 1

    x_abs = abs(x) 
    reversed_x = int(str(x_abs)[::-1])
    # reversed_x = reversed_x * sign
    reversed_x *= sign

    if reversed_x < -2 ** 31 or reversed_x > 2 ** 32 -1:
        return 0 

    return reversed_x
print(reverse(123))
print(reverse(-123))
print(reverse(10))