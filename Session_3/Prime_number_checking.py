check = 1

while check == 1:
    require = 1

    while require == 1:
        try:
            number = int(input("Enter a number: "))
            require = 0
        except ValueError:
            print("Int please!!!")
            print()
            require = 1
            continue
        if number < 1:
            print(">0 please!!!")
            print()
            require = 1

    prime = 0
    
    for i in range(number):
        if i == 0 or i == 1:
            continue
        elif number % i != 0:
            continue
        else:
            prime = 1
            divine = i
            break

    if prime == 0:
        print(number, "is not a prime number.")
    else:
        print(number, "is a prime number because {0}/{1} = {2}.".format(number, i, int(number / i)))
    print()

    again = input("Do you want to check again?(y/n) ").lower()
    while again != "n" and again != "y":
        again = input("Please answer yes or no!(y/n) ").lower()
        print()

    if again == "n":
        check = 0
        print()
        print("Bye!!!")
        print()
