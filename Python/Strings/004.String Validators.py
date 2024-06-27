#problem : https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    
    is_alnum = any(char.isalnum() for char in s)
    print(is_alnum)

# Check if the string has any alphabetical characters
    is_alpha = any(char.isalpha() for char in s)
    print(is_alpha)

# Check if the string has any digits
    is_digit = any(char.isdigit() for char in s)
    print(is_digit)

# Check if the string has any lowercase characters
    is_lower = any(char.islower() for char in s)
    print(is_lower)

# Check if the string has any uppercase characters
    is_upper = any(char.isupper() for char in s)
    print(is_upper)