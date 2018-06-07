factorial_calculate = 1

while factorial_calculate == 1:
    require = 1

    while require == 1:
        try:
            n = int(input("n=? "))
            require = 0
        except ValueError:
            print()
            print("Int please!!!")
            print()
            require = 1
            continue
        if n < 1:
            print()
            print(">0 please!!!")
            print()
            require = 1

    factorial_value = 1
    for i in range(n):
        factorial_value *= ( i + 1 )

    print()
    print("The facctorial of n is", factorial_value)
    print()
    
    again = input("Do you want to math again?(y/n) ").lower()
    while again != "n" and again != "y":
        again = input("Please answer yes or no!(y/n) ").lower()
        print()
                
    if again == "n":
        factorial_calculate = 0
        print()
        print("Bye!!!")
        print()

