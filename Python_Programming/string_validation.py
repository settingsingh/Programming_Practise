'''
Validating an input string if it has any of the following 
matching characters in it:
-alphanumeric
-alphabet
-digit
-lowercase
-uppercase

One way can be loop everytime in the string and check for the validations

But since python is known for its less lines of code speciality,
lets do it that way.

'''

string = input().strip()
for i in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
    print(any(eval("c." + i + "()") for c in string))
