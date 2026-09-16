# An Armstrong number is a number that equals the sum of its own digits, where each digit is raised to the power of the total number of digits.

def armstrong(n):
    num = n
    total = 0
    num_of_digits = len(str(n))
    while num > 0:
        last_digit = num % 10
        total = total + (last_digit ** num_of_digits)
        num = num // 10

    return total == n

print(armstrong(153))    