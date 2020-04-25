"""
The task of this problem is simple: insert a sequence of distinct positive integers into a hash table first. Then try to find another sequence of integer keys from the table and output the average search time (the number of comparisons made to find whether or not the key is in the table). The hash function is defined to be H(key)=key%TSize where TSize is the maximum size of the hash table. Quadratic probing (with positive increments only) is used to solve the collisions.

Note that the table size is better to be prime. If the maximum size given by the user is not prime, you must re-define the table size to be the smallest prime number which is larger than the size given by the user.
Input Specification:

Each input file contains one test case. For each case, the first line contains 3 positive numbers: MSize, N, and M, which are the user-defined table size, the number of input numbers, and the number of keys to be found, respectively. All the three numbers are no more than 10​4​​. Then N distinct positive integers are given in the next line, followed by M positive integer keys in the next line. All the numbers in a line are separated by a space and are no more than 10​5​​.
Output Specification:

For each test case, in case it is impossible to insert some number, print in a line X cannot be inserted. where X is the input number. Finally print in a line the average search time for all the M keys, accurate up to 1 decimal place.
Sample Input:

4 5 4
10 6 4 15 11
11 4 15 2

Sample Output:

15 cannot be inserted.
2.8
"""

#######################################################################
"""
考查平方探测法。
本题的坑点在于，不了解平方探测法的查找次数定义：
    当找不到数字时，则查找次数还要+1
    在这个点卡了很久！
"""


#######################################################################


def is_prime(num):
    for i in range(3, int(num ** 0.5), 2):
        if num % i == 0:
            return False
    else:
        return True


table_size, num_number, num_key = map(int, input().split())
if table_size <= 2:
    table_size = 2
elif table_size % 2 == 0:
    for table_size in range(table_size + 1, 20000, 2):
        if is_prime(table_size):
            break
else:
    for table_size in range(table_size, 20000, 2):
        if is_prime(table_size):
            break
hashing = [''] * table_size
for number in list(map(int, input().split())):
    for increment in range(table_size):
        pos = (number + increment * increment) % table_size
        if hashing[pos] == '':
            hashing[pos] = number
            break
    else:
        print(number, 'cannot be inserted.')
search_time = 0
for number in list(map(int, input().split())):
    for increment in range(table_size + 1):
        search_time += 1
        pos = (number + increment * increment) % table_size
        if hashing[pos] == number or hashing[pos] == '':
            break
print('%.1f' % (search_time / num_key))
