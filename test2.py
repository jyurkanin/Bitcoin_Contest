import binascii, hashlib, base58
from cryptos import *
from itertools import permutations
import decimal
import string
import sys

goal_address = "1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT"

def priv2addr(priv):
    pub = privtopub(priv)
    addr = pubtoaddr(pub)
    return (addr)

def padhex(s):
    return s[2:].rstrip('L').zfill(64)

def extend_master_key(chain_code, master_key):
    extended_58 = bip32_serialize((MAINNET_PRIVATE, 0, b'\x00'*4, 0, chain_code, master_key+b'\x01'))
    return binascii.hexlify(base58.b58decode(extended_58))
#    given = binascii.hexlify(base58.b58decode(bip32_master_key("a seed")))
#    metadata = given[0:26] #https://bitcoin.stackexchange.com/questions/78295/what-makes-an-extended-public-or-private-key
#    extended_master_private_key = metadata + binascii.unhexlify(chain_code) + b'00' + binascii.unhexlify(master_key)

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
    hex_private_key = hex(bigno)
    hex_private_key = hex_private_key[2:].rstrip('L')
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
alphabet = string.ascii_lowercase + string.ascii_uppercase

given_strings = ["BTC", "ETH", "XRP", "Phemex"]
ascii_list = []
for word in given_strings:
    ascii_string = ""
    for c in word:
        ascii_string = ascii_string + str(alphabet.index(c))
    ascii_list.append(ascii_string)


permutes = list(permutations(ascii_list))
print("permutes ", len(permutes))
for possibility in permutes:
    bigno = ""
    for word in possibility:
        bigno = bigno + str(word)

    print(len(bigno), bigno)
    #Ascii this bitch and concatenate ascii strings
    test_num = int(bigno)
    test(test_num)
    test(int(str(test_num) + str(prime)))
    test(int(str(prime) + str(test_num)))
    #Try ascii and multiplication
    test(test_num*prime)
    #ascii and xor
    test(test_num^prime)
    #ascii and add
    test(test_num+prime)
    
    #add more primes
    test(test_num*prime*prime)
    test(int(str(prime) + str(test_num) + str(prime)))
    test(int(str(prime) + str(prime) + str(test_num)))
    test(int(str(test_num) + str(prime) + str(prime)))
