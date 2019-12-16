def bs(A):
    dodai = len(A) - 1
    for a in range(dodai):
        for b in range(dodai - a):
            if A[b] < A[b+1]:
                A[b],A[b+1] = A[b+1], A[b]
    return A
A = [1,3,9,8,7,4,5]
H = bs(A)
print(H[::-1])
