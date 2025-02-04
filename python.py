# num = int(input("Enter: "))

# if num >= 55:
#     print("Yes")
#     if num == 100:
#         print("Num is 100")
#     # else if
# elif num == 40:
#         print("Num is 40")
# elif num == 46:
#     print("Num is")
# elif num < 4:
#     print("Num is less than 4")
# else:
#     print("Else") 

# ///////////////////

# isHappy = False
# if not isHappy:
#     print("Yes")

# //////////////////////

data = 'Info'
# 1
# if data == 'Info':
#     correct = True
# else:
#     correct = False

# print(correct)
# 2

# correct = True if data == 'Info' else False
# print(correct)

# //////////////////////////////////

# for i in range(5, 20, 7):
#     print("El ", i)

# //////////////////////////

# word = 'Some text'
# for i in word:
#     # print(i)
#     if i == 'm':
#         print('Літера м є в тексті')

# //////////////////////////////

# i = 100
# while i >= 10:
#     print(i)
#     i -= 10

work = True
while work:
        user_input = input("Enter word stop: ")
        if user_input == 'STOP' or user_input == 'stop':
            work = False
print("While loop is done")