"""
The Japanese language is notorious for its sentence ending particles. Personal preference of such particles can be considered as a reflection of the speaker's personality. Such a preference is called "Kuchiguse" and is often exaggerated artistically in Anime and Manga. For example, the artificial sentence ending particle "nyan~" is often used as a stereotype for characters with a cat-like personality:

    Itai nyan~ (It hurts, nyan~)

    Ninjin wa iyada nyan~ (I hate carrots, nyan~)

Now given a few lines spoken by the same character, can you find her Kuchiguse?
Input Specification:

Each input file contains one test case. For each case, the first line is an integer N (2≤N≤100). Following are N file lines of 0~256 (inclusive) characters in length, each representing a character's spoken line. The spoken lines are case sensitive.
Output Specification:

For each test case, print in one line the kuchiguse of the character, i.e., the longest common suffix of all N lines. If there is no such suffix, write nai.
Sample Input 1:

3
Itai nyan~
Ninjin wa iyadanyan~
uhhh nyan~

Sample Output 1:

nyan~


Sample Input 2:

3
Itai!
Ninjinnwaiyada T_T
T_T

Sample Output 2:

nai
"""

#####################################
"""
本题比较公共后缀字符串，可从末位逐一比较即可

将比较所得字符 逐一放入新的字符数组，代码会更加简洁

将字符串逆序，在代码写作方面可能会更加方便
"""
#####################################

N = int(input())
line = []
long = 9999999999
for _ in range(N):
    line.append(input())
    if len(line[-1]) < long:
        long = len(line[-1])
for i in range(1, long+1):
    compare = line[0][-i]
    same = True
    for j in range(1, N):
        if compare != line[j][-i]:
            same = False
            break
    if not same:
        break
if same:
    kuchiguse = line[0][-long:]
else:
    if i == 1:
        kuchiguse = 'nai'
    else:
        kuchiguse = line[0][-i+1:]
print(kuchiguse)
