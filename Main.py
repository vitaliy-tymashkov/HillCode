import unittest

from ServiceExample2 import encrypt
# from Service import encrypt

p = 'Five + Seven = Twelve'
k= 'math'

c = encrypt(p, k)
print ("Original key = ", k)
print ("Original plain text = ", p)
print ("Encrypted text = ", c)



