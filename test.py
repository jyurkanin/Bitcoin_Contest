import binascii, hashlib, base58
from bitcointools import *
import decimal

goal_address = "1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT"

def rotate(input,d): 
   # Slice string in two parts for left and right 
   Lfirst = input[0 : d] 
   Lsecond = input[d :] 
   Rfirst = input[0 : len(input)-d] 
   Rsecond = input[len(input)-d : ] 
   return(Lsecond + Lfirst)

def priv2addr(priv):
    pub = privtopub(priv)
    addr = pubtoaddr(pub)
    return (addr)

def padhex(s):
    return s[2:].rstrip('L').zfill(64)

def test(bigno):
    hex_private_key = padhex(hex(bigno)) 
    extended_key = "80"+hex_private_key.strip()
    first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
    second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
    final_key = extended_key+second_sha256[:8].encode()
    WIF = base58.b58encode(binascii.unhexlify(final_key)).decode()

    if (priv2addr(WIF) == goal_address):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print ("WIF: " + WIF)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return True
    print ("PKEY: " + hex_private_key.decode())
    return False

#A 	B 	C 	D 	E 	F 	G 	H 	I 	J 	K 	L 	M 	N 	O 	P 	Q 	R 	S 	T 	U 	V 	W 	X 	Y 	Z
#1 	2 	3 	4 	5 	6 	7 	8 	9 	10 	11 	12 	13 	14 	15 	16 	17 	18 	19 	20 	21 	22 	23 	24 	25 	26

prime = 957496696762772407663
XRP = 231715 #24*18*16
ETH = 4197 #5*20*8
BTC = 1192 #2*20*3
Phemex = 157412423 #16*8*5*13*5*24 # pheme mex
big_number= 95749669676277240766323171541971192157412423

test(big_number)
test(prime + XRP + ETH + BTC + Phemex)
test(prime * (XRP + ETH + BTC + Phemex))
test(prime * XRP * ETH * BTC * Phemex)
