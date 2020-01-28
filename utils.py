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
