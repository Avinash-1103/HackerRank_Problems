# Problem : https://www.hackerrank.com/challenges/py-the-captains-room/problem

from collections import Counter
K = int(input())
room_no = list(map(int, input().split()))

count = Counter(room_no)

for room, count in count.items():
    if count == 1:
        print(room)
        break
