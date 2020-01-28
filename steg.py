from PIL import Image
from collections import Counter
import matplotlib.pyplot as plt
import random
from utils_btc import *


image = Image.open("hate_it.jpeg").convert("YCbCr")


print image.getbands()

reds = image.getdata(0)   # "R" is 0
greens = image.getdata(1)  # "G" is 0
blues = image.getdata(2) # "B" is 0

len_pixels = len(reds)
reds_data = range(len_pixels)
greens_data = range(len_pixels)
blues_data = range(len_pixels)
diff_data = range(len_pixels)

offset = 0
for i in range(len_pixels):
    reds_data[i] = reds[i+offset]
    greens_data[i] = greens[i+offset]
    blues_data[i] = (blues[i+offset]-125)*20
    diff_data[i] = blues_data[i] - greens_data[i]




height = image.height
width = image.width   #len(gr_diff)/height
print height, width

#get_frequencies(output)

#blocks = get_blocks_from_image(reds_data, height, width)
#strings = collapse_blocks(blocks)
#byte_array = interpret_blocks_threshold(blocks, 127)

#scores = get_block_similarity(blocks, blocks[1200])

#flat = flatten_block(blocks[1200])

#unique_keys,frequencies = np.unique(greens_data, return_counts=True)

get_dct_coeff(image)


print "min", min(blues_data)
print "len", len(blues_data)
print "max", max(blues_data)

img = Image.frombytes('L', (width, height), str(bytearray(blues_data)))
#img.save("chroma.jpg")
img.show()

#plt.plot(reds_data, 'r', greens_data, 'g', blues_data, 'b')
#plt.plot(unique_keys, frequencies)
#steg_array = get_lowest_bits(reds_data, 1)
#steg_string = compile_lowest_bits(diff_data, 1)
#steg_array = get_frequencies(reds_data)

#plt.plot(reds_data)
#plt.plot(reds_data, 'r', blues_data, 'g', greens_data, 'b')
#plt.ylabel('steg test')
#plt.show()

