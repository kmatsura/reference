def binary_search(A, pivot, x, length):
    def up(x):
        if x > 1:
            return int(x)
        else:
            return 1
    print(pivot)
    if A[pivot] == x:
        print("Yes")
    elif length < 1/2:
        print("No")
    elif A[pivot] > x:
        if pivot == 0:
            print("No")
        else:
            return binary_search(A, pivot - up(length/2), x, length/2)
    elif A[pivot] < x:
        if pivot == len(A)-1:
            print("No")
        else:
            return binary_search(A, pivot + up(length/2), x, length/2)


A = [1, 3, 5, 6, 10]
n = len(A)
binary_search(A, int(n/2), 12, n/2)
