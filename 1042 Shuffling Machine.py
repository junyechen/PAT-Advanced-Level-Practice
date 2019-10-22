"""
Shuffling is a procedure used to randomize a deck of playing cards. Because standard shuffling techniques are seen as weak, and in order to avoid "inside jobs" where employees collaborate with gamblers by performing inadequate shuffles, many casinos employ automatic shuffling machines. Your task is to simulate a shuffling machine.

The machine shuffles a deck of 54 cards according to a given random order and repeats for a given number of times. It is assumed that the initial status of a card deck is in the following order:

S1, S2, ..., S13,
H1, H2, ..., H13,
C1, C2, ..., C13,
D1, D2, ..., D13,
J1, J2
where "S" stands for "Spade", "H" for "Heart", "C" for "Club", "D" for "Diamond", and "J" for "Joker". A given order is a permutation of distinct integers in [1, 54]. If the number at the i-th position is j, it means to move the card from position i to position j. For example, suppose we only have 5 cards: S3, H5, C1, D13 and J2. Given a shuffling order {4, 2, 5, 3, 1}, the result will be: J2, H5, D13, S3, C1. If we are to repeat the shuffling again, the result will be: C1, H5, S3, J2, D13.

Input Specification:

Each input file contains one test case. For each case, the first line contains a positive integer K (≤20) which is the number of repeat times. Then the next line contains the given order. All the numbers in a line are separated by a space.

Output Specification:

For each test case, print the shuffling results in one line. All the cards are separated by a space, and there must be no extra space at the end of the line.

Sample Input:

2
36 52 37 38 3 39 40 53 54 41 11 12 13 42 43 44 2 4 23 24 25 26 27 6 7 8 48 49 50 51 9 10 14 15 16 5 17 18 19 1 20 21 22 28 29 30 31 32 33 34 35 45 46 47
Sample Output:

S7 C11 C10 C12 S1 H7 H8 H9 D8 D9 S11 S12 S13 D10 D11 D12 S3 S4 S6 S10 H1 H2 C13 D2 D3 D4 H6 H3 D13 J1 J2 C1 C2 C3 C4 D1 S5 H5 H11 H12 C6 C7 C8 C9 S2 S8 S9 H10 D5 D6 D7 H4 H13 C5
"""


############################################
"""
非常简单，一次通过。
通过模拟重复即可。

另一种想法是通过矩阵相乘，但是在当前场景下过于复杂
"""
############################################

k = int(input())
c = [''] * 55
for i in range(1, 14):
    c[i] = 'S' + str(i)
for i in range(14, 27):
    c[i] = 'H' + str(i - 13)
for i in range(27, 40):
    c[i] = 'C' + str(i - 26)
for i in range(40, 53):
    c[i] = 'D' + str(i - 39)
for i in range(53, 55):
    c[i] = 'J' + str(i - 52)
card = [_ for _ in range(55)]
order = [int(_) for _ in input().split()]
order.insert(0, 0)
for _ in range(k):
    temp = card.copy()
    for i in range(1, 55):
        temp[order[i]] = card[i]
    card = temp.copy()
for i in card[1:54]:
    print(c[i], end=' ')
print(c[card[-1]])
