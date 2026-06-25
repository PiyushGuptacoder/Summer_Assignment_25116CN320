

def longest(str):
    words=str.split()
    longest_word=max(words,key=len)
    print("The longest word is: ",longest_word)

str=input("Enter the string: ")
# longest_word(str)
longest(str)