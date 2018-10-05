#Print 1-100, for divisible by 3 and 5 say FizzBuzz, for 3 say Fizz, for 5 say Buzz

x = 1
while x <= 100:
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
    x += 1
#
#         OR

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
#
#       OR


#create FizzBuzz using empty text
# text = ""
# for x in range(1, 101):
#     if x % 3 == 0:
#         print("%sFizz" % (text))
#     if x % 5 == 0:
#         print("%sBuzz" % (text))
#     print(x)
    