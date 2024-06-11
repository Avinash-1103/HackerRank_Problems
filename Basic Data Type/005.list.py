# problem : https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    # Initialize an empty list
    my_list = []

    # Number of commands
    n = int(input())

    # Read and process each command
    for _ in range(n):
        command = input().strip().split()
        cmd = command[0]

        if cmd == "insert":
            index = int(command[1])
            element = int(command[2])
            my_list.insert(index, element)
        elif cmd == "print":
            print(my_list)
        elif cmd == "remove":
            element = int(command[1])
            my_list.remove(element)
        elif cmd == "append":
            element = int(command[1])
            my_list.append(element)
        elif cmd == "sort":
            my_list.sort()
        elif cmd == "pop":
            if my_list:  # Check if the list is not empty
                my_list.pop()
        elif cmd == "reverse":
            my_list.reverse()