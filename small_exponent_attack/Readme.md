# Small exponent attack

This is one of the simplest attacks on RSA which arises when m^e is lesser than n.When this is the case, the modulo n loses it's significance and the encryption reduces to m^e (## Note: normal encryption is (m^e)%n).
Thus ct=m^e which implies m is the eth root of ct.
