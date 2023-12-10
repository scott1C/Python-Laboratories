def shortest_palindrome(string):
    reversed = string[::-1]
    for i in range(len(string)):
        if string.startswith(reversed[i:]):
            return reversed[:i] + string


string = input("Enter the string: ")
print(f"The palindrome for the '{string}' is: '{shortest_palindrome(string)}'")
