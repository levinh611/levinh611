def ms(A):
    H = len(A)
    if H > 1:
        middle = (H) // 2
        trai = A[:middle]
        phai = A[middle:]
        ms(trai)
        ms(phai)
        a = 0
        b = 0
        c = 0
        while a < len(trai) and b < len(phai):
           if trai[a] < phai[b]:
             A[c] = trai[a]
             a +=1
           else:
              A[c]= phai[b]
              b +=1
           c +=1
        while a < len(trai):
           A[c] = trai[a]
           a +=1
           c +=1
        while b < len(phai):
           A[c] = phai[b]
           b +=1
           c +=1
A = [34, 56, 78,3]
ms(A)
print(A[::-1])