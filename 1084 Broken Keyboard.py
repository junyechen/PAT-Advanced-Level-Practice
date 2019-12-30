"""
On a broken keyboard, some of the keys are worn out. So when you type some sentences, the characters corresponding to those keys will not appear on screen.

Now given a string that you are supposed to type, and the string that you actually type out, please list those keys which are for sure worn out.
Input Specification:

Each input file contains one test case. For each case, the 1st line contains the original string, and the 2nd line contains the typed-out string. Each string contains no more than 80 characters which are either English letters [A-Z] (case insensitive), digital numbers [0-9], or _ (representing the space). It is guaranteed that both strings are non-empty.
Output Specification:

For each test case, print in one line the keys that are worn out, in the order of being detected. The English letters must be capitalized. Each worn out key must be printed once only. It is guaranteed that there is at least one worn out key.
Sample Input:
7_This_is_a_test
_hs_s_a_es

Sample Output:
7TI
"""

###############################################
"""
非常简单，一次通过
1. 集合的操作，集合去重，求差集
    set1 = {1,2,3} set2 = {3,4,5}
    运算操作 	Python运算符 	含义 	                        例子
    交集 	    & 	            取两集合公共的元素 	            >>> set1 & set2
                                                                {3}
    并集 	    | 	            取两集合全部的元素 	            >>> set1 | set2
                                                                {1,2,3,4,5}
    差集 	    - 	            取一个集合中另一集合没有的元素 	>>> set1 - set2
                                                                {1,2}
                                                                >>> set2 - set1
                                                                {4,5}
    对称差集 	^ 	            取集合 A 和 B 中不属于 A&B 的元素 >>> set1 ^ set2
                                                                {1,2,4,5}
2. 按照原字符串顺序排序：
    sorted(res, key=line1.index)
"""
###############################################

line1 = input().upper()
line2 = input().upper()
# res = []
# for i in set(line1):
#     if i not in set(line2):
#         res.append(i)
res = list(set(line1) - set(line2))
print(''.join(sorted(res, key=line1.index)))
