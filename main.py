# Python 3.7
from random import randint
from time import time
import hashlib

# generate a list of size z
def generate_small_list():
    z = 11
    small_random_list = []
    for elem in range(1, z):
        small_random_list.append(randint(1, 3))

    return small_random_list

# compara two hashs of the same type
def compare_hash(hash1, hash2):
    if hash1 == hash2:
        print('Same object or the integrity is ok')
        return True
    else:
        print('The object is not the same or has been modified')
        return False

def get_hash_sha256(data):
    hash_data = hashlib.sha256(str(data).encode('utf-8')).hexdigest()
    return hash_data

def get_hash_md5(data):
    hash_data = hashlib.md5(str(data).encode('utf-8')).hexdigest()
    return hash_data

def get_hash_blake2s(data):
    hash_data = hashlib.blake2s(str(data).encode('utf-8')).hexdigest()
    return hash_data

def get_hash_shake128(data):
    hash_data = hashlib.shake_128(str(data).encode('utf-8')).hexdigest()
    return hash_data

times = 0
ans = False

print('Tip your option :')
print('1 >> md5')
print('2 >> sha256')
print('3 >> blake2s')

option = input('>> ')

if option == '1':
    hash_type = 'md5'
    hash_source = get_hash_md5(generate_small_list())
    start = time()
    while ans is False:
        hash_test = get_hash_md5(generate_small_list())
        ans = compare_hash(hash_source, hash_test)
        times += 1
        print(str(hash_source) + ' ' + str(hash_test) + ' ' + str(ans))
    end = time()
elif option == '2':
    hash_type = 'sha256'
    hash_source = get_hash_sha256(generate_small_list())
    start = time()
    while ans is False:
        hash_test = get_hash_sha256(generate_small_list())
        ans = compare_hash(hash_source, hash_test)
        times += 1
        print(str(hash_source) + ' ' + str(hash_test) + ' ' + str(ans))
    end = time()
elif option == '3':
    hash_type = 'blake2s'
    hash_source = get_hash_blake2s(generate_small_list())
    start = time()
    while ans is False:
        hash_test = get_hash_blake2s(generate_small_list())
        ans = compare_hash(hash_source, hash_test)
        times += 1
        print(str(hash_source) + ' ' + str(hash_test) + ' ' + str(ans))
    end = time()
else:
    print('choose a valid option:')

elapsed_time = end - start

print('Using ' + hash_type + ' :')
print('Times performed: ' + str(times))
print('Elapsed time: ' + str(elapsed_time))
print(get_hash_shake128(generate_small_list()))