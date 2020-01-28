import binascii, hashlib
from cryptos import *
from itertools import permutations
import decimal
import sys

goal_address = "1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT"

def priv2addr(priv):
    pub = privtopub(priv)
    addr = pubtoaddr(pub)
    return (addr)

def padhex(s):
    return s[2:].rstrip('L').zfill(64)

def test(bigno):
    hex_private_key = hex(bigno)
    test_key = hex_private_key[2:].rstrip('L').zfill(64)
    
    if(priv2addr(test_key) == goal_address):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print ("private key: " + str(bigno))
        print ("private key: " + str(test_key))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        sys.exit()
    return False

def main():
    prime = 957496696762772407663
    for i in range(100000, 1000000):
#    for i in range(0, 1000):
        print("Testing:", i)
        test(prime*i)
        test(int(str(prime)+str(i)))
        test(int(str(i)+str(prime)))


main()
    
