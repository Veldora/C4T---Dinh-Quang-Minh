import arithmetic_sequence as ex1
import exponential_list as ex2
import x_array as ex3
import absolute_sum as ex4

check_homework = 1

while check_homework == 1:
    require1 = 1

    while require1 == 1:
        homework = input("Which exercise do you want to check?(1, 2, 3, 4) ")
        require1 = 0
        if homework != "1" and homework != "2" and homework != "3" and homework != "4":
            print()
            print("Please answer 1 or 2 or 3 or 4!!!")
            require1 = 1
    
    if homework == "1":
        require2 = 1

        while require2 == 1:
            try:
                n = int(input("Enter a number: "))
                require2 = 0
            except ValueError:
                print()
                print("Please enter an integer!!!")
                require2 = 1
                continue
            if n < 1:
                print()
                print(">0 please!!!")
                require2 = 1

        print()
        n_list = ex1.arithmetic(n)

        print("Your list is:", end=" ")
        print(*n_list, sep=", ", end=".")
        print()
        
    elif homework == "2":
        exponential_list = ex2.exponential()
        print("Your list is:", end=" ")
        print(*exponential_list, sep=", ", end=".")
        print()

    elif homework == "3":
        require3c = 1

        while require3c == 1:
            try:
                length = int(input("How long is your list? "))
                require3c = 0
            except ValueError:
                print()
                print("Please enter an integer!!!")
                require3c = 1
                continue
            if length < 1:
                print()
                print(">0 please!!!")
                require3c = 1

        x_list = []
        for i in range(length):
            require3a = 1
            

            while require3a == 1:
                try:
                    num = float(input("Number " + str(i + 1) + ": "))
                    require3a = 0
                except ValueError:
                    print()
                    print("Please enter a float!!!")
                    require3a = 1
                    continue

            x_list.append(num)

        z_sum = ex3._arrays(x_list)
        print("The sum of elements of z is", z_sum)
        print()

    else:
        require3d = 1

        while require3d == 1:
            try:
                length = int(input("How long is your list? "))
                require3d = 0
            except ValueError:
                print()
                print("Please enter an integer!!!")
                require3d = 1
                continue
            if length < 1:
                print()
                print(">0 please!!!")
                require3d = 1

        x_list = []
        for i in range(length):
            require4a = 1
            

            while require4a == 1:
                try:
                    num = float(input("Number " + str(i + 1) + ": "))
                    require4a = 0
                except ValueError:
                    print()
                    print("Please enter a float!!!")
                    require4a = 1
                    continue

            x_list.append(num)

        abs_sum = ex4.absolute_sum(x_list)
        print("The sum of elements of the list is", abs_sum)
        print()

    print()
    again = input("Do you want to check again?(y/n) ").lower()
    while again != "n" and again != "y":
        again = input("Please answer yes or no!(y/n) ").lower()
        print()
                
    if again == "n":
        check_homework = 0
        print()
        print("Bye!!!")
        print()
