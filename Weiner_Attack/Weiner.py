from sage.all import *
N=90581
e=17993
m=14332
ct=pow(m,e,N)
arr1=(continued_fraction(e/N))
arr2=arr1.convergents()
for i in arr2:
    k=i.numerator()
    d=i.denominator()
    msg=pow(ct,d,N)
    if(msg==m):
        print(d)

