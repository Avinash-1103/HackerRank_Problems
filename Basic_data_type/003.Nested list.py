#problem : https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        
    sorted_list = sorted(records , key= lambda x:x[1])    
    
    second_lowest_grade = sorted(set(student[1] for student in sorted_list))[1]
    
    second_lowest_student = [student[0] for student in sorted_list if student[1] == second_lowest_grade]
    
    names = sorted(second_lowest_student)
    for student in names:
        print(student)