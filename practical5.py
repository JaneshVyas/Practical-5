# ID-20CS102    Name-Janesh Vyas

# You are given a string and your task is to swap cases. In other words, convert
# all lowercase letters to uppercase letters and vice versa.
# Sample Input: HackerRank.com presents "Pythonist 2".
 # Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".

 # function below takes a string as input and checks all letters in the string if letter is capital
 # it converts it into small and adds to reasult and if it is small it converts it into capital and adds
 # it to the reasult and if it is any number or symbol it adds it to reasult directly
def swapcase(word):
    answer=''
    for letter in word:
        if(letter.isupper()==True):
            answer=answer+(letter.lower())
        elif(letter.islower()==True):
            answer=answer+(letter.upper())
        else:
            answer=answer+letter
    return answer

input_string=input("Enter input:")
print(swapcase(input_string))
