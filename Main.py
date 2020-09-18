import unittest

from Service import encrypt

p = "Hi"
k = "cats"

p = 'This is a good day'
k= 'bbaa'

c = encrypt(p, k)
print (c)



