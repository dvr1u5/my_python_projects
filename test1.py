n = int(input())
count_3 = 0
lastdigit_count = 0
last_digit = n % 10
while n != 0:
    next_digit = n % 10
    n //= 10
    if next_digit == last_digit:
        lastdigit_count += 1
print(lastdigit_count)
