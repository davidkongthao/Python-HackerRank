"""

Problem: https://www.hackerrank.com/challenges/nested-list/problem

Given the names and grades for each student in a class of 'N' students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

"""

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    students = sorted(students, key = lambda x: x[1])
    second_lowest_score = sorted(list(set([x[1] for x in students])))[1]
    desired_students = []
    for stu in students:
        if stu[1] == second_lowest_score:
            desired_students.append(stu[0])
    print("\n".join(sorted(desired_students)))