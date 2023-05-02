A = list(map(int, input().split()))
B = list(map(int, input().split()))


def Intersection(A, B):
    NumList = list()
    i = 0
    j = 0
    while i + j < len(A) + len(B):
        if i < len(A) and j < len(B) and A[i] == B[j]:
            NumList.append(A[i])
            i += 1
            j += 1
        elif i < len(A) and j < len(B) and A[i] < B[j]:
            i += 1
        elif j < len(B) and i < len(A) and B[j] < A[i]:
            j += 1
        elif i >= len(A) and j < len(B):
            j += 1
        elif j >= len(B) and i < len(A):
            i += 1
    print(*NumList)


Intersection(A, B)
