# Temur Khabibullaev
# 11/02/2019
# Challenges get harder
# 1) Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input('Your name:\n>>> ')
age = input('Your age:\n>>> ')
years_left = 100 - int(age)
year_estimate = 2019 + years_left
print(f'Hi {name} ! In {year_estimate} you will turn 100 years old!')


# 2) Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
your_number = input("Give me a number and I'll detect whether it's odd or even.\n>>> ")
determination = int(your_number) % 2
if determination == 0:
    print('Even !')
else:
    print("Odd !")


# 3) Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest)
# and another number.
# The function decides whether or not the given number is inside the list
# and returns (then prints) an appropriate boolean.
list_of_numbers = [4, 10, 34, 45, 56, 100, 120, 3000]


def is_it_inside ():
    search_num = input("Give me a number, and I'll say whether it's inside my list.")
    if int(search_num) in list_of_numbers:
        print(True)
    else:
        print(False)


is_it_inside()


# 4) For this exercise, we will keep track of when our friend’s birthdays are,
# and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays.
# When you run your program it should ask the user to enter a name, and return the birthday of that person back to them
birthdays = {"Arthur": '10/15/1998', "Albert": '10/21/1999', "Temur": '12/10/1999', "Jared": "10/26/2000"}
persons_birthday = input("Whose birthday you need?")
if persons_birthday == "Arthur":
    print(birthdays["Arthur"])
if persons_birthday == "Albert":
    print(birthdays["Albert"])
if persons_birthday == "Temur":
    print(birthdays["Temur"])
if persons_birthday == "Jared":
    print(birthdays["Jared"])
else:
    print("I don't have his birthday.")


# 5) Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)
    else:
        break


# 6) Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
your_number = int(input("Give me a number, and I'll tell you its divisors!"))
eve = list(range(1, your_number + 1))
div_num = []
w = your_number % eve

