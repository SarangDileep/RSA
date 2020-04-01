import random
from Crypto.Util import number
alpha=50
p=number.getPrime(2048)
a=random.getrandbits(16)
b=random.getrandbits(16)
A=pow(alpha,a,p)
B=pow(alpha,b,p)
KAB=pow(B,a,p)
KBA=pow(A,b,p)
print(KBA)
print(KAB)
print(KAB==KBA)
