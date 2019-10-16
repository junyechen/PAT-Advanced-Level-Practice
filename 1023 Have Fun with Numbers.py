"""
Notice that the number 123456789 is a 9-digit number consisting exactly the numbers from 1 to 9, with no duplication. Double it we will obtain 246913578, which happens to be another 9-digit number consisting exactly the numbers from 1 to 9, only in a different permutation. Check to see the result if we double it again!

Now you are suppose to check if there are more numbers with this property. That is, double a given number with k digits, you are to tell if the resulting number consists of only a permutation of the digits in the original number.

Input Specification:

Each input contains one test case. Each case contains one positive integer with no more than 20 digits.

Output Specification:

For each test case, first print in a line "Yes" if doubling the input number gives a number that consists of only a permutation of the digits in the original number, or "No" if not. Then in the next line, print the doubled number.

Sample Input:

1234567899
Sample Output:

Yes
2469135798
"""


##############################
"""
本题用python做异常简单，因为不需要考虑数位、类型大小等问题
"""
##############################


num = input()
num_ = str(int(num)*2)
if len(num) != len(num_):
    print("No")
else:
    digit, digit_ = {}, {}
    for _ in range(10):
        digit[str(_)] = 0
        digit_[str(_)] = 0
    for _ in num:
        digit[_] += 1
    for _ in num_:
        digit_[_] += 1
    if digit_ == digit:
        print("Yes")
    else:
        print("No")
print(num_)
