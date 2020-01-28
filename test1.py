import binascii, hashlib, base58
from cryptos import *
from itertools import permutations
import decimal

goal_address = "1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT"

def priv2addr(priv):
    pub = privtopub(priv)
    addr = pubtoaddr(pub)
    return (addr)

def padhex(s):
    return s[2:].rstrip('L').zfill(64)

def test(bigno):
    hex_private_key = padhex(hex(bigno))
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
#print(p_list)
for possible in possibles:
    #Try b58decode then concatenation
    test_num = concat_ints(possible)
    test(int(str(test_num) + str(prime)))
    test(int(str(prime) + str(test_num)))

    #Try concatenation and multiplication
    test(test_num*prime)
    #concat and xor
    test(test_num^prime)
    #concat and add
    test(test_num+prime) 
    #add more primes
    test(test_num*prime*prime)
    test(int(str(prime) + str(test_num) + str(prime)))
    test(int(str(prime) + str(prime) + str(test_num)))
    test(int(str(test_num) + str(prime) + str(prime)))


given_strings = ["BTC", "ETH", "XRP", "Phemex"]
possible_strings = list(permutations(given_strings))
for possible in possible_strings:
    #concatenation then b58 decode
    test_string = concat_strings(possible)
    test_num = int(binascii.hexlify(base58.b58decode(test_string)), 16)
    test(test_num)
    test(int(str(prime) + str(test_num)))
    test(int(str(test_num) + str(prime)))
    
    #multiplication
    test(test_num*prime)
    #concat and xor
    test(test_num^prime) 
    #concat and add
    test(test_num+prime)
    #add more primes
    test(test_num*prime*prime)
    test(int(str(prime) + str(test_num) + str(prime)))
    test(int(str(prime) + str(prime) + str(test_num)))
    test(int(str(test_num) + str(prime) + str(prime)))
