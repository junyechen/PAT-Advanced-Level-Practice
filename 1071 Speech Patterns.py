"""
People often have a preference among synonyms of the same word. For example, some may prefer "the police", while others may prefer "the cops". Analyzing such patterns can help to narrow down a speaker's identity, which is useful when validating, for example, whether it's still the same person behind an online avatar.

Now given a paragraph of text sampled from someone's speech, can you find the person's most commonly used word?
Input Specification:

Each input file contains one test case. For each case, there is one line of text no more than 1048576 characters in length, terminated by a carriage return \n. The input contains at least one alphanumerical character, i.e., one character from the set [0-9 A-Z a-z].
Output Specification:

For each test case, print in one line the most commonly occurring word in the input text, followed by a space and the number of times it has occurred in the input. If there are more than one such words, print the lexicographically smallest one. The word should be printed in all lower case. Here a "word" is defined as a continuous sequence of alphanumerical characters separated by non-alphanumerical characters or the line beginning/end.

Note that words are case insensitive.
Sample Input:

Can1: "Can a can can a can?  It can!"

Sample Output:

can 5
"""

"""
本题新学习一些东西：
1. 可以用isalnum()来判断字符串中有无（字母、数字）
2. 可利用from collections import Counter，对列表中的项目进行计数
3. Counter.most_common(n)，为返回前n项最多的新项目列表与数目，返回值为元组
4. 本题中，可以利用isalnum()去除非字母符号，代以' '，而后利用split将各个单词划分区别
5. 本题中，利用python有可能还是会有超时现象
"""

'''
pattern = {}
for word in input().lower().split():
    for i in range(len(word)):
        if word[i].isalnum():
            break
    for j in range(len(word)-1, -1, -1):
        if word[j].isalnum():
            break
    if i <= j:
        word = word[i:j+1]
        try:
            pattern[word] += 1
        except:
            pattern[word] = 1
pattern = sorted(pattern.items(), key=lambda x: (-x[1], x[0]))
print(pattern[0][0], pattern[0][1])
'''


from collections import Counter

words = list(input().lower())
for i, j in enumerate(words):
    if j.isalnum():
        pass
    else:
        words[i] = ' '
words = ''.join(words)
count = Counter(words.split())
max_value = count.most_common(1)[0][1]
word = []
for key, value in count.items():
    if value == max_value:
        word.append(key)
word.sort()
print(word[0], max_value)


'''
from collections import Counter

line = [i for i in input()]
for i, j in enumerate(line):
    if not j.isalnum():
        line[i] = " "
line = "".join(line)
count = Counter(line.lower().split())
max = count.most_common(1)[0][1]
keys = sorted(count)
for i in keys:
    if count[i] == max:
        print(i, count[i])
'''