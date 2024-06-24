def minion_game(string):
    string.upper()
    user_1 = []
    user_2 = []

    all_permutations = []
    for i in range(len(string)):
        character = string[i]
        remaining = string[:i] + string[i+1:]
        for s in remaining:
            all_permutations.append(remaining + character)

    vowel = ["A","E","I","O","U"]  
    for j in all_permutations:
        if j in string:
            if j[0] in vowel:
                user_2.append(j)
            else:
                user_1.append(j)                
    print(all_permutations)
    print(user_1)
    print(user_2)            

STR = "BANANA"
minion_game(STR)        