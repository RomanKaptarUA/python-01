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

# work = True
# while work:
#         user_input = input("Enter word stop: ")
#         if user_input == 'STOP' or user_input == 'stop':
#             work = False
# print("While loop is done")

# /////////////////////////////////////////

# nums = [5, 7, 4, 5.45, True, 6]
# nums[0] = 34.34
# # print(nums[3])

# nums2 = [5, 7, 3, [5, "Text", True]]
# # print(nums2[-2])

# nums.append(45) #++++++++
# nums.insert(1, False) #False = 0, True = 1
# # nums.extend(nums2)
# nums.sort()
# # nums.reverse()
# print(nums)

# /////////////////////////////////////////////////

# nums = [5, 3, 2, 6.25]

# for el in nums:
#     res = el ** 2
#     print(res)

# ///////////////////////////////////////////////////
# while == допоки

# user_count_hobby = int(input("Enter hobby number: "))

# i = 0
# hobby = []
# while i < user_count_hobby:
#     text = "Enter hobby " + str(i + 1) + ": "
#     hobby.append(input(text))
    
#     i += 1

# print(hobby)

# ///////////////////////////////////////////////////////////

# word = list('itproger')
# word[0] = 'I'
# word.append('!')
# result = ''.join(word)
# print(word)
# print(len(word))

# print(result)
# print(result.upper())
# print(result.capitalize())
# print(result.lower())

# print(result.islower())
# print(result.isupper())

# ///////////////////////////////////////////////////////

# text = 'football,basketball,skate,drive'
# hobbies = text.split(',')

# for i in range(0, len(hobbies)): # від нуля до довжини hobbies
#     hobbies[i] = hobbies[i].capitalize()

# result = ", ".join(hobbies)
# print(result)

# /////////////////////////////////////////////////////////

# lis = [5, 3, True, "Some", [5, 4]]
# print(lis[1:5:2]) # перший параметр = (з) індексований, другий = (до) нормальний, третій = (крок)

# /////////////////////////////////////////////////////////////
# Кортежи = масив. В кортежі не можемо вносити зміни
# nums = [5, 6]
# data = tuple(nums)
# print(data) # перетворює масив в кортеж

# //////////////////////////////////////////////////////////////
# Словники
# person = {'name': 'Alex', 'age': 15, 5: 12, True: 'False'}
# person[5] = 'Five'
# print(person)
# print(person['age'])
# ///////////////////////////////////////////////////////////
# person1 = dict(name='Alex', age=15) # dict = dictionary
# print(person1)
# print(person1['name'])

# for i in person:
#     print(i)

# print(person.items())


# for key, values in person.items():
#       print(key, values, sep=" - ")

# for el in person.values():
#     print(el)

# ////////////////////////////////////////////////////////

# person =  {'name': 'Alex', 'age': 15, 5: 12, True: 'False'}
# print(person.get("name"))

# person['bio'] = 'Text' # щоб додати
# print(person)

# //////////////////////////////////////////////////////////
# Великий словник
people = {
  'user_1': {
     'name': 'John',
     'age': 27,
     'address': ('Мамаївці', 'Some street'),
     'grades': {'math': 5, 'physics': 5},
    },
    'user_2': {
      'surname': 'Doe',
      'name': 'Alex',
    }
}

print(people['user_1']['address'][1])