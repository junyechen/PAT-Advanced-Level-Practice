"""
People on Mars count their numbers with base 13:

    Zero on Earth is called "tret" on Mars.
    The numbers 1 to 12 on Earth is called "jan, feb, mar, apr, may, jun, jly, aug, sep, oct, nov, dec" on Mars, respectively.
    For the next higher digit, Mars people name the 12 numbers as "tam, hel, maa, huh, tou, kes, hei, elo, syy, lok, mer, jou", respectively.

For examples, the number 29 on Earth is called "hel mar" on Mars; and "elo nov" on Mars corresponds to 115 on Earth. In order to help communication between people from these two planets, you are supposed to write a program for mutual translation between Earth and Mars number systems.
Input Specification:

Each input file contains one test case. For each case, the first line contains a positive integer N (<100). Then N lines follow, each contains a number in [0, 169), given either in the form of an Earth number, or that of Mars.
Output Specification:

For each number, print in a line the corresponding number in the other language.
Sample Input:

4
29
5
elo nov
tam


Sample Output:

hel mar
may
115
13
"""

##########################################################################################################
"""
注意13,26时，低位“0”('tret)不显示
"""
##########################################################################################################

low_digit = ['tret', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec']
high_digit = ['', 'tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou']
for _ in range(int(input())):
    line = input()
    try:
        number = int(line)
        low = low_digit[number % 13]
        high = high_digit[number // 13]
        if high == '':
            print(low)
        else:
            if low == 'tret':
                print(high)
            else:
                print(high, low)
    except:
        if ' ' in line:
            first, last = line.split(' ')
            print(high_digit.index(first) * 13 + low_digit.index(last))
        else:
            try:
                print(low_digit.index(line))
            except:
                print(high_digit.index(line)*13)
