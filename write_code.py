code = 1

while code == 1:

    require = 1

    while require == 1:
        try:
            size = int(input("Enter the size? "))
            require = 0
        except ValueError:
            print()
            print("Int please!!!")
            print()
            require = 1
            continue
        if size < 5:
            print()
            print(">5 please!!!")
            print()
            require = 1

    for y in range(size):
        for x in range((size + 2) * 4 - 2):
            if y == 0 or y == size - 1:
                if 0 <= x <= size - 1 or size + 2 <= x <= size * 2 + 1 or size * 2 + 4 <= x <= size * 3 + 2 or size * 3 + 6 <= x <= size * 4 + 5:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif y == int((size - 1) / 2):
                if x == 0 or x == size + 2 or x == size * 2 + 1 or x == size * 2 + 4 or x == size * 3 + 3 or size * 3 + 6 <= x <= size * 4 + 5:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            else:
                if x == 0 or x == size + 2 or x == size * 2 + 1 or x == size * 2 + 4 or x == size * 3 + 3 or x == size * 3 + 6:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()

    again = input("Do you want to write again?(y/n) ").lower()
    while again != "n" and again != "y":
        again = input("Please answer yes or no!(y/n) ").lower()
        print()
                
    if again == "n":
        code = 0
        print()
        print("Bye!!!")
        print()
