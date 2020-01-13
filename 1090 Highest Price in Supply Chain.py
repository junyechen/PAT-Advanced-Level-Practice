"""
A supply chain is a network of retailers（零售商）, distributors（经销商）, and suppliers（供应商）-- everyone involved in moving a product from supplier to customer.

Starting from one root supplier, everyone on the chain buys products from one's supplier in a price P and sell or distribute them in a price that is r% higher than P. It is assumed that each member in the supply chain has exactly one supplier except the root supplier, and there is no supply cycle.

Now given a supply chain, you are supposed to tell the highest price we can expect from some retailers.
Input Specification:

Each input file contains one test case. For each case, The first line contains three positive numbers: N (≤10​5​​), the total number of the members in the supply chain (and hence they are numbered from 0 to N−1); P, the price given by the root supplier; and r, the percentage rate of price increment for each distributor or retailer. Then the next line contains N numbers, each number S​i​​ is the index of the supplier for the i-th member. S​root​​ for the root supplier is defined to be −1. All the numbers in a line are separated by a space.
Output Specification:

For each test case, print in one line the highest price we can expect from some retailers, accurate up to 2 decimal places, and the number of retailers that sell at the highest price. There must be one space between the two numbers. It is guaranteed that the price will not exceed 10​10​​.

Sample Input:
9 1.80 1.00
1 5 4 4 -1 4 5 3 6

Sample Output:
1.85 2
"""

####################################
"""
本题即为求图的最大深度，题目告知父节点，可将其转换成子节点，便于计算
若用传统dfs递归方法，测试数据过多会造成迭代次数超过python限制（为非零返回），需更改，但是仍有错误（内存超限）
可借用队列的方法进行层序遍历，非递归方式，测试点6通过，但测试点1、2超时，不得不寻求C++的帮助
"""
####################################

n, p, r = input().split()
n, p, r = int(n), float(p), float(r)
road_up = map(int, input().split())
road_down = {}
for i, j in enumerate(road_up):
    try:
        road_down[j].append(i)
    except:
        road_down[j] = [i]
depth = 0
child = road_down[-1]
while child:
    retail = len(child)
    temp = []
    for root in child:
        if root in road_down:
            temp += road_down[root]
    child = temp
    depth += 1
print('%0.2f' % (p*(1+r/100)**(depth-1)), retail)

'''
#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
int n, maxdepth = 0, maxnum = 0, temp, root;
vector<int> v[100010];
void dfs(int index, int depth) {
    if(v[index].size() == 0) {
        if(maxdepth == depth)
            maxnum++;
        if(maxdepth < depth) {
            maxdepth = depth;
            maxnum = 1;
        }
        return ;
    }
    for(int i = 0; i < v[index].size(); i++)
        dfs(v[index][i], depth + 1);
}
int main() {
    double p, r;
    scanf("%d %lf %lf", &n, &p, &r);
    for(int i = 0; i < n; i++) {
        scanf("%d", &temp);
        if(temp == -1)
            root = i;
        else
            v[temp].push_back(i);
    }
    dfs(root, 0);
    printf("%.2f %d", p * pow(1 + r/100, maxdepth), maxnum);
    return 0;
}
'''

'''
import sys


def dfs(root, depth):
    global max_depth, max_retail, road_down
    if root in road_down:
        for child in road_down[root]:
            dfs(child, depth + 1)
    else:
        if max_depth < depth:
            max_depth = depth
            max_retail = 1
        elif max_depth == depth:
            max_retail += 1


sys.setrecursionlimit(10000)
n, p, r = input().split()
n, p, r = int(n), float(p), float(r)
road_up = map(int, input().split())
road_down = {}
for i, j in enumerate(road_up):
    try:
        road_down[j].append(i)
    except:
        road_down[j] = [i]
max_depth = -1
max_retail = 0
dfs(-1, -1)
print('%0.2f' % (p*(1+r/100)**max_depth), max_retail)
'''
