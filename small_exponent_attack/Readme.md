# Small exponent attack

This is one of the simplest attacks on RSA which arises when pow(m,e,n) is lesser than m.When this is the case, the modulo n loses it's significance and the encryption reduces to m^e.
Thus ct=m^e which implies m is the eth root of ct.
