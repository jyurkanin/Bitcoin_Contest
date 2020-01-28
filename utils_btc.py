from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import entropy
import binascii
import copy
from PIL import Image

from numpy import pi
from numpy import sin
from numpy import zeros
from numpy import r_
from scipy import signal
from scipy import misc
import matplotlib.pylab as pylab
import scipy.fftpack


def get_frequencies_rgb(reds, greens, blues):
    unique_keys_r = Counter(reds).keys()
    frequencies_r = Counter(reds).values()

    unique_keys_b = Counter(blues).keys()
    frequencies_b = Counter(blues).values()

    unique_keys_g = Counter(greens).keys()
    frequencies_g = Counter(greens).values()

    plt.plot(frequencies_r, 'r', frequencies_g, 'g', frequencies_b, 'b')
    
    plt.xlabel('Keys')
    plt.ylabel('Frequencies')
#    plt.title("Distribution of values for RGB over the whole thing")
    plt.show()


def get_frequencies(data):
    unique_keys,frequencies = np.unique(data, return_counts=True)
    print "min", min(frequencies)
    print "len", len(frequencies)
    print "max", max(frequencies)
#    unique_keys = Counter(data).keys()
#    frequencies = Counter(data).values()

    print unique_keys, frequencies
    
#    plt.plot(unique_keys[1:-1], frequencies[1:-1])
    plt.plot(frequencies)
        
    plt.xlabel('Keys')
    plt.ylabel('Frequencies')
    plt.title("Distribution of reds - greens over background")
    plt.show()

#input is numbers
#it takes the lowest bits. Makes them into a string of bits
#chops the string into bytes
#returns a sequence of ascii

def compile_lowest_bits(data, bit_depth):
    bin_string = ""
    for datum in data:
        bin_string = bin_string + bin(int(datum) & ((1 << bit_depth) - 1)).replace('0b', '')

    #output_string = ""
    #for i in range(0, len(bin_string), 8):
    #    output_string = output_string + chr(int(bin_string[i:i+8], 2))
    output_array = []
    for i in range(0, len(bin_string), 8):
        output_array.append(int(bin_string[i:i+8], 2))
    return output_array

#input data, bit_depth 1 means take the lowest bit off every num. 2 means the lowest 2 bits...
#output array of the lowest bits.

def get_lowest_bits(data, bit_depth):
    temp = []
    for datum in data:
        temp.append(datum & ((1 << bit_depth) - 1))
    return temp

        
def entropy1(labels):
  value,counts = np.unique(labels, return_counts=True)
  return entropy(counts)

def get_n_grams(data, n):
    gram_list = []
    for i in range(0, len(data), n):
        gram_list.append(str(data[i:i+n]))
    return gram_list
    

def xor_data(data, key):
    output_data = range(len(data))
    key_hex = hex(key).replace("0x", "").replace("L", "")

    key_bytes = []
    for i in range(0, len(key_hex), 2):
        key_bytes.append(ord(binascii.unhexlify(key_hex[i:i+2])))
    
    
    for i in range(len(data)):
        output_data[i] = data[i] ^ key_bytes[i % len(key_bytes)]
    
    return output_data

def get_blocks_from_image(data, height, width):    
    h_offset = 0
    w_offset = 0
    h_end = height
    w_end = width

    block_array = []
    block = np.zeros((8, 8)).tolist()
    for y in range(h_offset, h_end-8, 8):
        for x in range(w_offset, w_end-8, 8):
            for w in range(8):
                for h in range(8):
                    block[w][h] = data[w+x][y+h]
            block_array.append(copy.deepcopy(block))
    return block_array

def collapse_blocks(blocks):
    strings = []
    for block in blocks:
        sum_block = ""
        for x in block:
            for y in x:
                sum_block = sum_block + str(y) + "_"
        strings.append(sum_block)
    return strings

def interpret_blocks_lsb(blocks, sig_bit):
    byte_array = []
    for block in blocks:
        num = 0
        for row in block:
            for col in row:
                if(col & (1 << sig_bit)):
                    num = num + 1
        byte_array.append(num)
    return byte_array

def interpret_blocks_threshold(blocks, cutoff):
    byte_array = []
    for block in blocks:
        num = 0
        for row in block:
            for col in row:
                if(col > cutoff):
                    num = num + 1
        byte_array.append(num)
    return byte_array

def flatten_block(block):
    out = []
    for row in block:
        for col in row:
            out.append(col)
    return out

def get_block_similarity(blocks, test):
    test_flat = flatten_block(test)
    print "block size ", test_flat
    img = Image.frombytes('L', (16, 16), str(bytearray(test_flat)))
    img.show()
    
    scores = []
    for block in blocks:
        score = 0
        for row in range(len(block)):
            for col in range(len(block)):
                temp = block[row][col] - test[row][col]
                if(temp != 0):
                    score = score + 1
        scores.append(score)
    return scores

def dct2(a):
    a_norm = copy.deepcopy(a)
    for x in range(len(a)):
        for y in range(len(a[0])):
            a_norm[x][y] = a[x][y] - 127
    
    return scipy.fftpack.dct( scipy.fftpack.dct( a_norm, axis=0, norm='ortho' ), axis=1, norm='ortho' )

def get_dct_coeff(im, bs): # bs is 8 or 16
    imsize = im.shape
    dct = np.zeros(imsize)
    output_dct = np.zeros(imsize, dtype=int)
    
    #djpeg -verbose -verbose foo.jpg > /dev/null
    lumin_quant_table = np.array([5, 3, 3, 5, 7, 12, 15, 18, 4, 4, 4, 6, 8, 17, 18, 17, 4, 4, 5, 7, 12, 17, 21, 17, 4, 5, 7, 9, 15, 26, 24, 19, 5, 7, 11, 17, 20, 33, 31, 23, 7, 11, 17, 19, 24, 31, 34, 28, 15, 19, 23, 26, 31, 36, 36, 30, 22, 28, 29, 29, 34, 30, 31, 30])
    chrome_quant_table = np.array([5, 5, 7, 14, 30, 30, 30, 30, 5, 6, 8, 20, 30, 30, 30, 30, 7, 8, 17, 30, 30, 30, 30, 30, 14, 20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30])

    lumin_quant_table = lumin_quant_table.reshape(8, 8)
    chrome_quant_table = chrome_quant_table.reshape(8, 8)
    table = chrome_quant_table

    width = imsize[0]
    height = imsize[1]
    
    for i in r_[:imsize[0]:bs]:
        for j in r_[:imsize[1]:bs]:
            dct[i:(i+bs),j:(j+bs)] = dct2( im[i:(i+bs),j:(j+bs)] )
            for x in range(8):
                for y in range(8):
                    if((i+x) < width and (j+y) < height ):
                        output_dct[i+x][j+y] = int(dct[i+x][j+y] / table[x][y])
    
    return output_dct

def get_symmetry_score(x_list, y_list):
    score = 0
    for i in range(len(x_list)):
        if(x_list[i] == 0):
            break
        for j in range(len(x_list)):
            if(x_list[i] == -x_list[j]):
                print "Diff", abs(y_list[i] - y_list[j])
                score = score + abs(y_list[i] - y_list[j])
    print "Symmetry:", score


def print_block(dct, x, y):
    tempx = x*8
    tempy = y*8
    
    for i in range(tempy,tempy+8):
        line = ""
        for j in range(tempx,tempx+8):
            line = line + str(dct[i][j]) + " "
        print line
    print ""

def get_dc_offsets(dct):
    dcs = []
    for i in range(0, dct.shape[0], 8):
        for j in range(0, dct.shape[1], 8):
            dcs.append(dct[i][j])
    return dcs

def convert_to_string(dct):
    s = ""
    for i in dct:
        s = s + str(i)
    return s

def convert_to_bytes(dct):
    l = []
    for i in range(0, len(dct)-8, 8):
        temp = ""
        for j in range(8):
            num = dct[j+i]
            if(num == 1):
                temp = temp + "0"
            if(num == 2):
                temp = temp + "1"
            if(num == 3):
                temp = temp + "0"
            if(num == 4):
                temp = temp + "1"
        l.append(int(temp, 2))
    return l

def get_bit_array(dcs):
    l = []
    for i in dcs:
        if(i == 1):
            l.append(0)
            l.append(0)
        if(i == 2):
            l.append(64)
            l.append(0)
        if(i == 3):
            l.append(0)
            l.append(64)
        if(i == 4):
            l.append(64)
            l.append(64)
    return l
