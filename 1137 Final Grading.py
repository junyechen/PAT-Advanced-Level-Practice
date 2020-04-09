"""
For a student taking the online course "Data Structures" on China University MOOC (http://www.icourse163.org/), to be qualified for a certificate, he/she must first obtain no less than 200 points from the online programming assignments, and then receive a final grade no less than 60 out of 100. The final grade is calculated by G=(G​mid−term​​×40%+G​final​​×60%) if G​mid−term​​>G​final​​, or G​final​​ will be taken as the final grade G. Here G​mid−term​​ and G​final​​ are the student's scores of the mid-term and the final exams, respectively.

The problem is that different exams have different grading sheets. Your job is to write a program to merge all the grading sheets into one.
Input Specification:

Each input file contains one test case. For each case, the first line gives three positive integers: P , the number of students having done the online programming assignments; M, the number of students on the mid-term list; and N, the number of students on the final exam list. All the numbers are no more than 10,000.

Then three blocks follow. The first block contains P online programming scores G​p​​'s; the second one contains M mid-term scores G​mid−term​​'s; and the last one contains N final exam scores G​final​​'s. Each score occupies a line with the format: StudentID Score, where StudentID is a string of no more than 20 English letters and digits, and Score is a nonnegative integer (the maximum score of the online programming is 900, and that of the mid-term and final exams is 100).
Output Specification:

For each case, print the list of students who are qualified for certificates. Each student occupies a line with the format:

StudentID G​p​​ G​mid−term​​ G​final​​ G

If some score does not exist, output "−1" instead. The output must be sorted in descending order of their final grades (G must be rounded up to an integer). If there is a tie, output in ascending order of their StudentID's. It is guaranteed that the StudentID's are all distinct, and there is at least one qullified student.
Sample Input:

6 6 7
01234 880
a1903 199
ydjh2 200
wehu8 300
dx86w 220
missing 400
ydhfu77 99
wehu8 55
ydjh2 98
dx86w 88
a1903 86
01234 39
ydhfu77 88
a1903 66
01234 58
wehu8 84
ydjh2 82
missing 99
dx86w 81

Sample Output:

missing 400 -1 99 99
ydjh2 200 98 82 88
dx86w 220 88 81 84
wehu8 300 55 84 84
"""

################################################################
"""
非常简单，一次通过
"""
################################################################


def main():
    num_online, num_mid, num_final = map(int, input().split())
    database = {}
    for _ in range(num_online):
        ID, score = input().split()
        score = int(score)
        if score < 200:
            pass
        else:
            database[ID] = [score, -1, -1, 0]
    for _ in range(num_mid):
        ID, score = input().split()
        if ID in database:
            database[ID][1] = int(score)
    for _ in range(num_final):
        ID, score = input().split()
        if ID in database:
            database[ID][2] = int(score)
    del_key = []
    for key in database.keys():
        score_mid, score_final = database[key][1:3]
        if score_mid > score_final:
            score = score_mid * 0.4 + score_final * 0.6
            score = int(score + 0.5)
        else:
            score = score_final
        if score >= 60:
            database[key][3] = score
        else:
            del_key.append(key)
    for key in del_key:
        database.pop(key)
    database = [[keys] + values for keys, values in database.items()]
    database.sort(key=lambda x: (-x[4], x[0]))
    for record in database:
        print(' '.join(map(str, record)))


if __name__ == '__main__':
    main()
