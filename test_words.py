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

def test_derp(bigno):
    if(bigno == 0):
        return
    
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
words = [["BITCOIN", "Bitcoin", "bitcoin",  "BTC", "Btc", "btc"],         ["ETHEREUM", "Ethereum", "ethereum", "ETH", "Eth", "eth"],         ["RIPPLE", "Ripple", "ripple", "XRP", "Xrp", "xrp"],         ["PHEMEX", "Phemex", "phemex"]]
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
for num_permutations in range(1, 4):
    print("Permutes ", num_permutations)
    line_counter = 0
    for line in all_capitalizations:
        print("line ", line_counter, "/", len(all_capitalizations))
        line_counter = line_counter + 1
        possibles = list(permutations(line, num_permutations))
        for possible in possibles:
            test_string = ""
            for word in possible:
                test_string = test_string + word
            
            #These use products to make a big int
            add_to_global_set(string_to_ascii_product(test_string))
            add_to_global_set(string_to_nocase_alphabet_index_product(test_string))
            add_to_global_set(string_to_lu_case_alphabet_index_product(test_string))
            add_to_global_set(string_to_ul_case_alphabet_index_product(test_string))
            add_to_global_set(string_to_b58_product(test_string))
            
            #These use concatenation of strings to make a big int
            add_to_global_set(string_to_nocase_alphabet_index_concat(test_string))
            add_to_global_set(string_to_lu_case_alphabet_index_concat(test_string))
            add_to_global_set(string_to_ul_case_alphabet_index_concat(test_string))
            add_to_global_set(string_to_b58_concat(test_string))
            
            #This is a direct b58 conversion
            add_to_global_set(string_to_b58(test_string))

            #These ones do c % 21 for each character in string and then compute product
            add_to_global_set(string_to_b58_mod_p(test_string))
            add_to_global_set(string_to_ascii_mod_p(test_string))
            add_to_global_set(string_to_alpha_mod_p(test_string))

            #These ones do c % 21 for each character in string and then concatenate 
            add_to_global_set(string_to_b58_mod_cat(test_string))
            add_to_global_set(string_to_ascii_mod_cat(test_string))
            add_to_global_set(string_to_alpha_mod_cat(test_string))
            
        
print("Len without repeats", len(all_test_numbers))
input("Press Enter Please")

for i in all_test_numbers:
    test_with_prime(i)

#for i in all_test_numbers:
#    if(len(str(i)) == 27):
#        print(i)
#    print(len(str(i)), i)
