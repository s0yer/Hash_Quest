# Python 3.7
from random import randint
from time import time
import hashlib

def generate_small_list():
    small_random_list = []
    for elem in range(1, 11):
        small_random_list.append(randint(1, 3))

    return small_random_list

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

start = time()
times = 0
ans = False
while ans is False:
    list1 = generate_small_list()
    list2 = generate_small_list()
    ans = compare_hash(get_hash_sha256(list1), get_hash_sha256(list2))
    times += 1
    print(str(list1) + str(list2) + str(ans))
end = time()
elapsed_time = end - start

print('Using sha256: ')
print('Times performed: ' + str(times))
print('Elapsed time: ' + str(elapsed_time))
