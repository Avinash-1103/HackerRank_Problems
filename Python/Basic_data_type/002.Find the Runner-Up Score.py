#Problem : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores = list(set(arr))  
    unique_scores.sort()  
    if len(unique_scores) < 2:
        print("Not enough unique scores to determine a runner-up.")
    else:
        print(unique_scores[-2])      