from random import *
count = 1

while count == 1:
    numbers = []
    for i in range(10):
        random_number = randrange(0, 10)
        numbers.append(random_number)

    print("My list is:", end=" ")
    print(*numbers, sep=", ")
    print()

    require = 1

    while require == 1:
        try:
            number_check = int(input("Enter a number? "))
            require = 0
        except ValueError:
            print("Please enter a number!!!")
            print()
            require = 1

##    with count() function:     numbers.count(number_check))

    appears = 0
    
    for i in range(len(numbers)):
        if numbers[i] == number_check:
            appears += 1
        else:
            continue

    print("{0} appears {1} times in my list.".format(number_check, appears))
    print()

    again = input("Do you want to do this again?(y/n) ").lower()
    while again != "n" and again != "y":
        again = input("Please answer yes or no!(y/n) ").lower()
        print()

    if again == "n":
        count = 0
        print()
        print("Bye!!!")
    print()
