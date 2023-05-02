A = list(map(int, input().split()))
B = list(map(int, input().split()))
NumList = list()


def merge(A, B):
    i = 0
    j = 0
    while i + j < len(A) + len(B):
        if i < len(A) and j < len(B) and A[i] <= B[j]:
            NumList.append(A[i])
            i += 1
        elif j < len(B) and i < len(A) and B[j] <= A[i]:
            NumList.append(B[j])
            j += 1
        elif i >= len(A) and j < len(B):
            NumList.append(B[j])
            j += 1
        elif j >= len(B) and i < len(A):
            NumList.append(A[i])
            i += 1
    print(*NumList)


merge(A, B)
