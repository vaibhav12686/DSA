# hashing - prestoring values into some data structure like list/set/dictionary and then fetching it

# brute force

def hashing(n, m):
    for x in m:
        count = 0

        for y in n:
            if y == x:
                count += 1
        print(count)


hashing([5,3,2,2,1,5,5,7,5,10], [10,111,1,9,5,67,2])


# optimal

# create a hash list of size 11

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

hash_list = [0] * 11
for num in n:
    hash_list[num] += 1

for num in m:
    if num < 1 or num > 10:
        print(0)

    else:
        print(hash_list[num])



# character hashing

# constraints
# 'a' <= s[i] <= 'z'


s = "azyxyyzaaaa"
q = ["a", "a", "y", "x"]

hash_list = [0] * 26

for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hash_list[index] += 1

for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(hash_list[index])
