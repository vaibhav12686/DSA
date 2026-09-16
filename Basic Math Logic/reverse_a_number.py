# using string slicing

n = 1234
rev = int(str(n)[::-1])
print(rev)



# using while loop

n = 6789
rev = 0

while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n //= 10

print(rev)



# using for loop

n = 6789
rev = ''

for ch in str(n):
    rev = ch + rev

print(int(rev))



# using recursion

def rev_num(n):
    if n < 10:
        return n
    return int(str(n % 10) + str(rev_num(n // 10)))

n = 987654
print(rev_num(n))