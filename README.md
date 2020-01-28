Bitcoin Contest
This repository is mainly to document my slow descent into madness.
In the off chance that this repo was useful for you and helped you
win the phemex bitcoin contest, then give me money damnit.

jpeg_steg.py, steg.py, and utils_btc.py are related to my attempts
at uncovering steganographic data from the image. I didn't find
anything. I worked for days generating histograms and learning about
the JPEG compression algorithm until the first hints dropped and I
started looking for this 27 digit number.

test_words.py has the most recent attempt.
In that file, I use the array
words = [["BITCOIN", "Bitcoin", "bitcoin",  "BTC", "Btc", "btc"],
         ["ETHEREUM", "Ethereum", "ethereum", "ETH", "Eth", "eth"],
         ["RIPPLE", "Ripple", "ripple", "XRP", "Xrp", "xrp"],
         ["PHEMEX", "Phemex", "phemex"]]

To list the different spellings I'm willing to investigate.
Then I try permutations, using groups of 1, 2, 3, and 4 words from
the list concatenated together. With each grouping of words,
I apply different strategies to convert them into 27 digit numbers.
You can see the functions used to convert from strings to numbers
in the file utils.py. There are numerous.

I am unsure how to combine the 27 digit number with the prime number
so I try a number of different strategies including modulus, xor,
addition, multiplication, division, and string concatenation. The
result is a big number.

I am also not sure how to convert the big number into a private key.
So, I try a few methods.
First, I try to just convert the big number into hex and pad it with
leading zeros to create the private key.
Next, I try to convert the big number into 64 bytes with leading zeros,
and I hash the result with sha256 to get the private key.
Third, I convert the big number to a string and convert the string
to a list of ascii bytes and hash it with sha256.

Doesn't really seem to work though.