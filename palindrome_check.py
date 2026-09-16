def palindrome(n):
    num = n
    result = 0
    while num > 0:
        last_digit = num % 10
        result = (result * 10) + last_digit
        num = num // 10
    if n == result:
        return True
    else:
        return False

print(palindrome(962269))
    