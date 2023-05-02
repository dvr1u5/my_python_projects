# put your python code here
n = int(input())
count = 0
left = 1
right = n
while left != right:
    middle = (left + right) // 2 + 1
    right = middle - 1
    count += 1
print(count)
