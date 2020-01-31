import binascii, hashlib, base58
from cryptos import *
from itertools import permutations
from itertools import combinations
import decimal
import copy
import string
import sys
import hashlib

from utils import *

goal_address = "1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT"
prime = 957496696762772407663

all_test_numbers = set() #no repeats

def add_to_global_set(thing):
    if(len(str(thing)) == 27):
        all_test_numbers.add(thing)

def priv2addr(priv):
    pub = privtopub(priv)
    addr = pubtoaddr(pub)
    return (addr)

def padhex(s):
    return s[2:].rstrip('L').zfill(64)

def test_bip32(bigno):
    if(bigno == 0):
        return
    
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

def test(bigno):
    hex_private_key = padhex(hex(bigno))
    print("PKEY", hex_private_key)
    if(priv2addr(hex_private_key) == goal_address):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print ("private key: " + str(bigno))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        sys.exit()
    
    hex_private_key = hashlib.sha256(bigno.to_bytes(64, byteorder='big').strip(b'\x00')).hexdigest()
    print("PKEY", hex_private_key)
    if(priv2addr(hex_private_key) == goal_address):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print ("private key: " + str(bigno))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        sys.exit()


    hex_private_key = hashlib.sha256(str(bigno).encode("ascii")).hexdigest()
    print("PKEY", hex_private_key)
    if(priv2addr(hex_private_key) == goal_address):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print ("private key: " + str(bigno))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        sys.exit()


        
def test_with_prime(smallno):
    prime_combos = []
    prime_combos.append(prime*smallno)
    prime_combos.append(int(str(prime) + str(smallno)))
    prime_combos.append(int(str(smallno) + str(prime)))
    prime_combos.append(prime+smallno)
    prime_combos.append(prime^smallno)
    prime_combos.append(int(prime/smallno))
    
    prime_combos.append(smallno*prime*prime)
    prime_combos.append(int(str(prime) + str(smallno) + str(prime)))
    prime_combos.append(int(str(prime) + str(prime) + str(smallno)))
    prime_combos.append(int(str(smallno) + str(prime) + str(prime)))
    prime_combos.append(smallno % prime)
    prime_combos.append(prime % smallno)
    for i in prime_combos:
        test(i)
        
#words = [["BITCOIN", "Bitcoin", "bitcoin",  "BTC", "BTc", "Btc", "BtC", "bTC", "bTc", "btC", "btc"],         ["ETHEREUM", "Ethereum", "ethereum", "ETH", "ETh", "EtH", "Eth", "eTH", "eTh", "etH", "eth"],         ["RIPPLE", "Ripple", "ripple", "XRP", "XRp", "XrP", "Xrp", "xRP", "xRp", "xrP", "xrp"],         ["PHEMEX", "Phemex", "phemex"], ["PRIME", "Prime", "prime"], ["EULER", "Euler", "euler"]]
words = [["BITCOIN", "Bitcoin", "bitcoin",  "BTC", "Btc", "btc"],         ["ETHEREUM", "Ethereum", "ethereum", "ETH", "Eth", "eth"],         ["RIPPLE", "Ripple", "ripple", "XRP", "Xrp", "xrp"],         ["PHEMEX", "Phemex", "phemex", "FMX", "fmx"]]
all_capitalizations = [] #try every possible way to capitalize the words and create a 2d array of them.

#There has got to be a better way to do this.
for i in range(len(words[0])):
    for j in range(len(words[1])):
        for k in range(len(words[2])):
            for m in range(len(words[3])):
                word_list = [0,0,0,0]
                word_list[0] = words[0][i]
                word_list[1] = words[1][j]
                word_list[2] = words[2][k]
                word_list[3] = words[3][m]
                all_capitalizations.append(word_list)


#This does combinations
for num_combos in range(1, 4):
    print("Combos ", num_combos)
    line_counter = 0
    for line in all_capitalizations:
        print("line ", line_counter, "/", len(all_capitalizations))
        line_counter = line_counter + 1
        possibles = list(combinations(line, num_combos))
        for possible in possibles:
            test_string = ""
            for word in possible:
                test_string = test_string + word
            add_to_global_set(string_to_b58_primes(test_string))
            add_to_global_set(string_to_alpha_lu_primes(test_string))
            add_to_global_set(string_to_alpha_ul_primes(test_string))
            
        
print("Len without repeats", len(all_test_numbers))
input("Press Enter Please")

for i in all_test_numbers:
    test_with_prime(i)
