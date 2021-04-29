'''
This file aims to shuffle a playlist in a given directory.
Personal use: shuffle playlist of songs in headphones with MP3 player without option to shuffle
'''

### Imports
import os
from tqdm import tqdm
from random import randint

# Directory containing your playlist
data_dir = 'D:/'

def shuffle_playlist():
    '''
    This function aims to shuffle a playlist in a given directory
    '''
    number_files = len(os.listdir(data_dir))
    num_digits = len(str(number_files))

    for filename in tqdm(os.listdir(data_dir)):
        rand_num = randint(1,number_files)
        str_rand = '0'*(num_digits - len(str(rand_num))) + str(rand_num)
        if filename[0] == '_':
            os.rename(data_dir + filename, data_dir + filename[num_digits+2:])
            filename = filename[num_digits+2:]
        os.rename(data_dir + filename, data_dir + '_' + str_rand + '_' + filename)

# Main
shuffle_playlist()