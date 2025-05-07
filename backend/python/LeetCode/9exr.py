def isPalindrome(x: int) -> bool:
    x_abs = abs(x) 
    reversed_x = int(str(x_abs)[::-1])

    if reversed_x < -2 ** 31 or reversed_x > 2 ** 32 -1:
        return False
    if reversed_x == x:
        return True
    return False
print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
