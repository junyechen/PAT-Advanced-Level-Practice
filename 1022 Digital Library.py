"""
A Digital Library contains millions of books, stored according to their titles, authors, key words of their abstracts, publishers, and published years. Each book is assigned an unique 7-digit number as its ID. Given any query from a reader, you are supposed to output the resulting books, sorted in increasing order of their ID's.

Input Specification:

Each input file contains one test case. For each case, the first line contains a positive integer N (≤10
​4
​​ ) which is the total number of books. Then N blocks follow, each contains the information of a book in 6 lines:

Line #1: the 7-digit ID number;
Line #2: the book title -- a string of no more than 80 characters;
Line #3: the author -- a string of no more than 80 characters;
Line #4: the key words -- each word is a string of no more than 10 characters without any white space, and the keywords are separated by exactly one space;
Line #5: the publisher -- a string of no more than 80 characters;
Line #6: the published year -- a 4-digit number which is in the range [1000, 3000].
It is assumed that each book belongs to one author only, and contains no more than 5 key words; there are no more than 1000 distinct key words in total; and there are no more than 1000 distinct publishers.

After the book information, there is a line containing a positive integer M (≤1000) which is the number of user's search queries. Then M lines follow, each in one of the formats shown below:

1: a book title
2: name of an author
3: a key word
4: name of a publisher
5: a 4-digit number representing the year
Output Specification:

For each query, first print the original query in a line, then output the resulting book ID's in increasing order, each occupying a line. If no book is found, print Not Found instead.

Sample Input:

3
1111111
The Testing Book
Yue Chen
test code debug sort keywords
ZUCS Print
2011
3333333
Another Testing Book
Yue Chen
test code sort keywords
ZUCS Print2
2012
2222222
The Testing Book
CYLL
keywords debug book
ZUCS Print2
2011
6
1: The Testing Book
2: Yue Chen
3: keywords
4: ZUCS Print
5: 2011
3: blablabla
Sample Output:

1: The Testing Book
1111111
2222222
2: Yue Chen
1111111
3333333
3: keywords
1111111
2222222
3333333
4: ZUCS Print
1111111
5: 2011
1111111
2222222
3: blablabla
Not Found
"""


########################################
"""
本题非常简单，只是需要重复输入类似的代码块，1次通过
"""
########################################


num = int(input())
ID = []
book_title = {}
author = {}
key_words = {}
publisher = {}
publish_year = {}
for _ in range(num):
    ID.append(input())
    temp = input()
    if temp in book_title:
        book_title[temp].append(ID[-1])
    else:
        book_title[temp] = [ID[-1]]
    temp = input()
    if temp in author:
        author[temp].append(ID[-1])
    else:
        author[temp] = [ID[-1]]
    temp = input().split()
    for i in temp:
        if i in key_words:
            key_words[i].append(ID[-1])
        else:
            key_words[i] = [ID[-1]]
    temp = input()
    if temp in publisher:
        publisher[temp].append(ID[-1])
    else:
        publisher[temp] = [ID[-1]]
    temp = input()
    if temp in publish_year:
        publish_year[temp].append(ID[-1])
    else:
        publish_year[temp] = [ID[-1]]
M = int(input())
for _ in range(M):
    code, line = input().split(':')
    print(code + ':' + line)
    if code == '1':
        book_title_ = line[1:]
        if book_title_ in book_title:
            for i in list(sorted(book_title[book_title_])):
                print(i)
        else:
            print("Not Found")
    elif code == '2':
        author_ = line[1:]
        if author_ in author:
            for i in list(sorted(author[author_])):
                print(i)
        else:
            print("Not Found")
    elif code == '3':
        key_words_ = line[1:]
        if key_words_ in key_words:
            for i in list(sorted(key_words[key_words_])):
                print(i)
        else:
            print("Not Found")
    elif code == '4':
        publisher_ = line[1:]
        if publisher_ in publisher:
            for i in list(sorted(publisher[publisher_])):
                print(i)
        else:
            print("Not Found")
    elif code == '5':
        publish_year_ = line[1:]
        if publish_year_ in publish_year:
            for i in list(sorted(publish_year[publish_year_])):
                print(i)
        else:
            print("Not Found")
