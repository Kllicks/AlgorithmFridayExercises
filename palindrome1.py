import string

user_list = input("Give a word to check if it is a palindrome: ").lower()

def palindrome(user_list):
    user_list = user_list.replace(" ", "")
    user_list = user_list.replace(",", "")
    palindrome_list = user_list[::-1]
    if user_list == palindrome_list:
        print("this is a palindrome")
    else:
        print("this is not a palindrome")

palindrome(user_list)