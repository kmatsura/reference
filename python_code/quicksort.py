import sys
import random

def main():
    n = int(input())
    A = list(map(int, input().split()))
    qsort(A, 0, n-1)
    print(*A)

def qsort(seq, _l, _r):
    l = _l
    r = _r
    cent = int((l+r)/2)
    pivot = seq[cent]
    print(seq, l, r, pivot)
    if (r - l) == 1:
        if seq[r] < seq[l]:
            seq[l], seq[r] = seq[r], seq[l]
            return seq
    if l >= r:
        return seq
    while(l < r):
        if seq[l] >= pivot and seq[r] <= pivot:
            seq[l], seq[r] = seq[r], seq[l]
            l += 1
            r -= 1
        elif seq[l] < pivot and seq[r] >= pivot:
            l += 1
            r -= 1
        elif seq[l] < pivot and seq[r] < pivot:
            l += 1
        elif seq[l] >= pivot and seq[r] >= pivot:
            r -= 1
    if l == _l or r == _r:
        return seq
    seq = qsort(seq, _l, cent)
    seq = qsort(seq, cent, _r)
    return seq
if __name__ == '__main__':
    main()
