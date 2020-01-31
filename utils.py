import string
import base58
import binascii

lower_upper = string.ascii_lowercase + string.ascii_uppercase
upper_lower = string.ascii_uppercase + string.ascii_lowercase





def string_to_b58(word):
    cleaned = word.replace("0", "")
    cleaned = cleaned.replace("O", "")
    cleaned = cleaned.replace("I", "")
    cleaned = cleaned.replace("l", "")    
    return int(binascii.hexlify(base58.b58decode(cleaned)), 16)







def string_to_ascii_product(word):
    product = 1
    for c in word:
        product = product * ord(c)
    return product

def string_to_nocase_alphabet_index_product(word):
    product = 1
    temp = word.lower()
    for c in temp:
        product = product * string.ascii_lowercase.index(c)
    return product

def string_to_ul_case_alphabet_index_product(word):
    product = 1
    for c in word:
        product = product * upper_lower.index(c)
    return product

def string_to_lu_case_alphabet_index_product(word):
    product = 1
    for c in word:
        product = product * lower_upper.index(c)
    return product

def string_to_b58_product(word):
    product = 1
    for c in word:
        if(c =="0" or c == "O" or c == "l" or c == "I"):
            continue
        product = product * int(binascii.hexlify(base58.b58decode(c)), 16)
    return product






def string_to_ascii_mod_p(word):
    product = 1
    for c in word:
        product = product * (ord(c) % 21)
    return product

def string_to_alpha_mod_p(word):
    product = 1
    temp = word.lower()
    for c in temp:
        product = product * (string.ascii_lowercase.index(c) % 21)
    return product

def string_to_b58_mod_p(word):
    product = 1
    for c in word:
        if(c =="0" or c == "O" or c == "l" or c == "I"):
            continue
        product = product * (int(binascii.hexlify(base58.b58decode(c)), 16) %21)
    return product



    



def string_to_nocase_alphabet_index_concat(word):
    concat = ""
    temp = word.lower()
    for c in temp:
        concat = concat + str(string.ascii_lowercase.index(c))
    return int(concat)

def string_to_ul_case_alphabet_index_concat(word):
    concat = ""
    for c in word:
        concat = concat + str(upper_lower.index(c))
    return int(concat)

def string_to_lu_case_alphabet_index_concat(word):
    concat = ""
    for c in word:
        concat = concat + str(lower_upper.index(c))
    return int(concat)

def string_to_b58_concat(word):
    concat = ""
    for c in word:
        if(c =="0" or c == "O" or c == "l" or c == "I"):
            continue
        concat = concat + str(int(binascii.hexlify(base58.b58decode(c)), 16))
    return int(concat)










def string_to_alpha_mod_cat(word):
    concat = ""
    temp = word.lower()
    for c in temp:
        concat = concat + str(string.ascii_lowercase.index(c) % 21)
    return int(concat)

def string_to_b58_mod_cat(word):
    concat = ""
    for c in word:
        if(c =="0" or c == "O" or c == "l" or c == "I"):
            continue
        concat = concat + str(int(binascii.hexlify(base58.b58decode(c)), 16) % 21)
    return int(concat)

def string_to_ascii_mod_cat(word):
    concat = ""
    for c in word:
        concat = concat + str(ord(c) % 21)
    return int(concat)


#this is gonna be some cicada shit where I
#convert all letters into primes and multiply
#them all together
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

#this is going to get the alphabet index of each character, and use that index to select the prime, and multiply shit together
def string_to_alpha_primes(word):
    product = 1
    temp = word.lower()
    for c in temp:
        product = product * primes[string.ascii_lowercase.index(c)]
    return product

def string_to_alpha_lu_primes(word):
    product = 1
    for c in word:
        product = product * primes[lower_upper.index(c)]
    return product

def string_to_alpha_ul_primes(word):
    product = 1
    for c in word:
        product = product * primes[lower_upper.index(c)]
    return product

def string_to_b58_primes(word):
    product = 1
    for c in word:
        if(c =="0" or c == "O" or c == "l" or c == "I"):
            continue
        product = product * primes[int(binascii.hexlify(base58.b58decode(c)), 16)]
    return product
        
