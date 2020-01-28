import string
import base58
import binascii
from cryptos import *
import decimal
import hashlib

goal_address = "1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT"

def priv2addr(priv):
    pub = privtopub(priv)
    addr = pubtoaddr(pub)
    return (addr)

def padhex(s):
    return s[2:].rstrip('L').zfill(64)

def test(bigno):
    test_hexify(bigno)
    hex_private_key = str(bigno)
#    hex_private_key = hex_private_key[2:].rstrip('L')
    print("PKEY", hex_private_key)
    for i in range(64):
        if(len(hex_private_key) > 64):
            break
        test_key = hex_private_key.zfill(64)
        if(priv2addr(test_key) == goal_address):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print ("private key: " + str(bigno))
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            sys.exit()
        hex_private_key = hex_private_key + "0"

def test_hexify(bigno):
    print("Number ", bigno)
    hex_private_key = hex(bigno)
    hex_private_key = hex_private_key[2:].rstrip('L')
    for i in range(64):
        if(len(hex_private_key) > 64):
            break
        test_key = hex_private_key.zfill(64)
        if(priv2addr(test_key) == goal_address):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print ("private key: " + str(bigno))
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            sys.exit()
        hex_private_key = hex_private_key + "0"

prime = 957496696762772407663
alphabet = string.ascii_lowercase

given_strings = ["BTC", "ETH", "XRP", "Phemex"]
num_list = []
for word in given_strings:
    num = 1
    for c in word:
        num = num * alphabet.index(c.lower())
    num_list.append(num)

alpha_sum = 0
for word in num_list:
    alpha_sum = alpha_sum + word
    
alpha_xor = 0
for word in num_list:
    alpha_xor = alpha_xor ^ word

test(alpha_xor)
test(alpha_xor*prime)
test(int(str(alpha_xor) + str(prime)))
test(int(str(prime) + str(alpha_xor)))

test(alpha_sum)
test(alpha_sum*prime)
test(int(str(alpha_sum) + str(prime)))
test(int(str(prime) + str(alpha_sum)))

