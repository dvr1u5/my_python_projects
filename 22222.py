k = int(input())
if k > 1:
    for i in range(2, int(k/2)+1):
         if (k % i) == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")

else:
    print("It is not a prime number")