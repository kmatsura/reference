import sys
## まだ動かない

def main():
    n = int(input())
    A = list(map(int, input().split()))
    qsort(A, 0, n-1)
    print(*A)

def qsort(seq, _l, _r):
    l = _l
    r = _r
    pivot = seq[int(l+r/2)]
    while(l < r):
        if seq[l] >= pivot and seq[r] < pivot:
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
    left = seq[_l:l]
    right = seq[l:_r]
    print(left, right)
    if len(left) <= 1 and len(right) <= 1:
        return seq
    else:
        seq = qsort(seq, 0, l)
        seq = qsort(seq, l, r)
if __name__ == '__main__':
    main()
