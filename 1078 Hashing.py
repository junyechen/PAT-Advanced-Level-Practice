"""
The task of this problem is simple: insert a sequence of distinct positive integers into a hash table, and output the positions of the input numbers. The hash function is defined to be H(key)=key%TSize where TSize is the maximum size of the hash table. Quadratic probing (with positive increments only) is used to solve the collisions.

Note that the table size is better to be prime. If the maximum size given by the user is not prime, you must re-define the table size to be the smallest prime number which is larger than the size given by the user.
Input Specification:

Each input file contains one test case. For each case, the first line contains two positive numbers: MSize (≤10​4​​) and N (≤MSize) which are the user-defined table size and the number of input numbers, respectively. Then N distinct positive integers are given in the next line. All the numbers in a line are separated by a space.
Output Specification:

For each test case, print the corresponding positions (index starts from 0) of the input numbers in one line. All the numbers in a line are separated by a space, and there must be no extra space at the end of the line. In case it is impossible to insert the number, print "-" instead.
Sample Input:

4 4
10 6 4 15

Sample Output:

0 1 4 -
"""

##############################################
"""
学习了哈希表的平方探测法（quadratic probing），即hash(key) = (key+step*step)%size，（题目要求步长为正整数，当地址有冲突时，step逐渐增长，纸质找到无冲突的地址或者step超过size）

新学习了python这样的语句：
    for ```:
        ```
    else:
        ```
该语句中else的用法为：当for循环为正常结束时，执行else里的语句；若for循环break跳出后，则不执行else中的语句

这题一开始后面2个测试点出现错误，结果发现增大素数表的范围就解决了= =！，说好的数据<=10^4呢？浪费了我好多时间！
"""
##############################################

primes = [1]*100001
primes[0], primes[1] = 0, 0
for i in range(4, 100001, 2):
    primes[i] = 0
for i in range(3, int(100001**0.5), 2):
    if primes[i] == 1:
        for j in range(i*3, 100001, i*2):
            primes[j] = 0

msize, n = map(int, input().split())
if primes[msize] == 0:
    for i in range(msize+1, 100001):
        if primes[i] == 1:
            msize = i
            break

H = [0 for _ in range(msize)]
res = []
for key in map(int, input().split()):
    # found = False
    for di in range(msize):
        index_ = (key+di*di) % msize
        if H[index_] == 0:
            H[index_] = 1
            # found = True
            res.append(index_)
            break
    # if not found:
    else:
        res.append('-')
print(' '.join(list(map(str, res))))
