from utils_btc import *
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

image = Image.open("neuromancer.jpg").convert("YCbCr")
y_data = image.getdata(1)
y_np = np.array(y_data)
y_mat = y_np.reshape(image.width, image.height)

dct = get_dct_coeff(y_mat, 8)
#DC = get_dc_offsets(dct)


width = image.width
height = image.height

print height, width

#byte_list = convert_to_bytes(DC)

#lsb_array = compile_lowest_bits(dct.flatten(), 0)
#print lsb_array
get_frequencies(dct.flatten())


#bits = get_bit_array(DC)
#print len(bits)
#tw = int(raw_input("width "))
#th = len(bits)/tw
#img = Image.frombytes('L', (width, height), str(bytearray(dct)))
#img.save("chrome_dct.jpg")
#img.show()


#blocks = get_blocks_from_image(dct, height, width)
#strings = collapse_blocks(blocks)

#unique_keys,frequencies = np.unique(byte_list, return_counts=True)
#print unique_keys, frequencies
#plt.plot(unique_keys, frequencies)
#plt.show()
#get_symmetry_score(unique_keys, frequencies)
