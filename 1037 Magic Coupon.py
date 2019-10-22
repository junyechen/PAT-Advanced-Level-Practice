"""
The magic shop in Mars is offering some magic coupons. Each coupon has an integer N printed on it, meaning that when you use this coupon with a product, you may get N times the value of that product back! What is more, the shop also offers some bonus product for free. However, if you apply a coupon with a positive N to this bonus product, you will have to pay the shop N times the value of the bonus product... but hey, magically, they have some coupons with negative N's!

For example, given a set of coupons { 1 2 4 −1 }, and a set of product values { 7 6 −2 −3 } (in Mars dollars M$) where a negative value corresponds to a bonus product. You can apply coupon 3 (with N being 4) to product 1 (with value M$7) to get M$28 back; coupon 2 to product 2 to get M$12 back; and coupon 4 to product 4 to get M$3 back. On the other hand, if you apply coupon 3 to product 4, you will have to pay M$12 to the shop.

Each coupon and each product may be selected at most once. Your task is to get as much money back as possible.

Input Specification:

Each input file contains one test case. For each case, the first line contains the number of coupons N
​C
​​ , followed by a line with N
​C
​​  coupon integers. Then the next line contains the number of products N
​P
​​ , followed by a line with N
​P
​​  product values. Here 1≤N
​C
​​ ,N
​P
​​ ≤10
​5
​​ , and it is guaranteed that all the numbers will not exceed 2
​30
​​ .

Output Specification:

For each test case, simply print in a line the maximum amount of money you can get back.

Sample Input:

4
1 2 4 -1
4
7 6 -2 -3
Sample Output:

43
"""


############################################
"""
非常简单，一次通过
可能考察大数计算，但是python可以完全无视，且给出数据无超时
"""
############################################


cou_p, cou_n, pro_p, pro_n = [], [], [], []
input()
cou = [int(_) for _ in input().split()]
for i in cou:
    if i < 0:
        cou_n.append(-i)
    elif i > 0:
        cou_p.append(i)
input()
pro = [int(_) for _ in input().split()]
for i in pro:
    if i < 0:
        pro_n.append(-i)
    elif i > 0:
        pro_p.append(i)
cou_p.sort(reverse=True)
cou_n.sort(reverse=True)
pro_p.sort(reverse=True)
pro_n.sort(reverse=True)
i = 0
maximum = 0
while i < len(cou_p) and i < len(pro_p):
    maximum += cou_p[i] * pro_p[i]
    i += 1
i = 0
while i < len(cou_n) and i < len(pro_n):
    maximum += cou_n[i] * pro_n[i]
    i += 1
print(maximum)