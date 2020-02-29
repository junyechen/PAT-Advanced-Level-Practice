"""
This time, you are supposed to help us collect the data for family-owned property. Given each person's family members, and the estate（房产）info under his/her own name, we need to know the size of each family, and the average area and number of sets of their real estate.
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤1000). Then N lines follow, each gives the infomation of a person who owns estate in the format:

ID Father Mother k Child​1​​⋯Child​k​​ M​estate​​ Area

where ID is a unique 4-digit identification number for each person; Father and Mother are the ID's of this person's parents (if a parent has passed away, -1 will be given instead); k (0≤k≤5) is the number of children of this person; Child​i​​'s are the ID's of his/her children; M​estate​​ is the total number of sets of the real estate under his/her name; and Area is the total area of his/her estate.
Output Specification:

For each case, first print in a line the number of families (all the people that are related directly or indirectly are considered in the same family). Then output the family info in the format:

ID M AVG​sets​​ AVG​area​​

where ID is the smallest ID in the family; M is the total number of family members; AVG​sets​​ is the average number of sets of their real estate; and AVG​area​​ is the average area. The average numbers must be accurate up to 3 decimal places. The families must be given in descending order of their average areas, and in ascending order of the ID's if there is a tie.
Sample Input:

10
6666 5551 5552 1 7777 1 100
1234 5678 9012 1 0002 2 300
8888 -1 -1 0 1 1000
2468 0001 0004 1 2222 1 500
7777 6666 -1 0 2 300
3721 -1 -1 1 2333 2 150
9012 -1 -1 3 1236 1235 1234 1 100
1235 5678 9012 0 1 50
2222 1236 2468 2 6661 6662 1 300
2333 -1 3721 3 6661 6662 6663 1 100

Sample Output:

3
8888 1 1.000 1000.000
0001 15 0.600 100.000
5551 4 0.750 100.000
"""

########################################################
"""
再次涉及了并查集，第一时间没有反应过来，还想着建树遍历来做
巩固复习
"""
########################################################


class Info:
    def __init__(self, ID):
        self.ID = ID
        self.owner = ID
        self.estate_num = 0
        self.estate_area = 0
        self.family_num = 1


def main():
    n = int(input())
    people = [Info(_) for _ in range(10000)]
    for _ in range(n):
        info = list(map(int, input().split()))
        if info[3] == 0:
            family = info[:3]
        else:
            family = info[:3] + info[4:4+info[3]]
        if family[1] == -1 and family[2] == -1:
            family.pop(1)
            family.pop(1)
        elif family[1] == -1:
            family.pop(1)
        elif family[2] == -1:
            family.pop(2)
        owner_list = []
        for member in family:
            temp_owner = member
            while people[temp_owner].owner != temp_owner:
                temp_owner = people[temp_owner].owner
            owner_list.append(temp_owner)
        min_id = min(set(owner_list))
        for member in family:
            temp_owner = member
            while people[temp_owner].owner != temp_owner:
                temp_owner = people[temp_owner].owner
            if min_id < temp_owner:
                people[temp_owner].owner = min_id
                people[member].owner = min_id
                people[min_id].estate_area += people[temp_owner].estate_area
                people[min_id].estate_num += people[temp_owner].estate_num
                people[min_id].family_num += people[temp_owner].family_num
                people[temp_owner].estate_area = 0
                people[temp_owner].estate_num = 0
                people[temp_owner].family_num = 0
        people[min_id].estate_num += info[-2]
        people[min_id].estate_area += info[-1]
    assemble_data = {}
    for i in range(10000):
        if people[i].estate_num != 0:
            owner = i
            while people[owner].owner != owner:
                owner = people[owner].owner
            assemble_data[owner] = [people[i].family_num, people[i].estate_num, people[i].estate_area]
    res = []
    for key, value in assemble_data.items():
        res.append([key] + value)
    res.sort(key=lambda x: (-x[3]/x[1], x[0]))
    print(len(res))
    for r in res:
        print("%04d %d %.3f %.3f" % (r[0], r[1], r[2]/r[1], r[3]/r[1]))


if __name__ == '__main__':
    main()
