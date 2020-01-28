import binascii, hashlib, base58
from cryptos import *
from itertools import permutations
import decimal
import string
import sys

prime = 957496696762772407663
goal_address = "1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT"

def priv2addr(priv):
    pub = privtopub(priv)
    addr = pubtoaddr(pub)
    return (addr)

def padhex(s):
    return s[2:].rstrip('L').zfill(64)

def test(bigno):
    private_master_bip = bip32_master_key(str(prime)) #seed with the 27 digit number
    private_child_bip = bip32_ckd(private_master_bip, bigno) #get the prime number'th child key
    test_key = bip32_extract_key(private_child_bip)
    test_key = test_key[:-2]
    
    print("PKEY", test_key)
    if(priv2addr(test_key) == goal_address):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print ("private key: " + str(bigno))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        sys.exit()

def concat_ints(i_list):
    sum = ""
    for i in i_list:
        sum = sum + str(i)
    return int(sum)

def concat_strings(s_list):
    sum = ""
    for s in s_list:
        sum = sum + s
    return sum

def multiply_all(l_nums):
    num = 1
    for l in l_nums:
        num = num * l
    return num


prime = 957496696762772407663
XRP = int(binascii.hexlify(base58.b58decode("XRP")), 16) # converted from base58 to base10
ETH = int(binascii.hexlify(base58.b58decode("ETH")), 16)
BTC = int(binascii.hexlify(base58.b58decode("BTC")), 16)
Phemex = int(binascii.hexlify(base58.b58decode("Phemex")), 16)
p_list = [Phemex, BTC, ETH, XRP]
possibles = list(permutations(p_list))

for possible in possibles:
    #Try b58decode then concatenation
    test_num = concat_ints(possible)
    if(len(str(test_num)) == 27):
        test(test_num)

given_strings = ["BTC", "ETH", "XRP", "Phemex"]
possible_strings = list(permutations(given_strings))
for possible in possible_strings:
    #concatenation then b58 decode
    test_string = concat_strings(possible)
    test_num = int(binascii.hexlify(base58.b58decode(test_string)), 16)
    if(len(str(test_num)) == 27):
        test(test_num)
