bmi_calculate = 1

while bmi_calculate == 1:
    require = 1

    while require == 1:
        try:
            height = float(input("What is your height(cm)? "))
            weight = float(input("What is your weight(kg)? "))
            require = 0
        except ValueError:
            print()
            print("Float please!!!")
            print()
            require = 1
            continue
        if height <= 0 or weight <= 0:
            print()
            print(">0 please!!!")
            print()
            require = 1

    height = height / 100
    bmi_value = weight / ( height ** 2 )

    print()
    print("Your BMI value is", bmi_value)
    print()
    if bmi_value < 16:
        print("You are severely underweight.")
    elif bmi_value >= 16 and bmi_value <= 18.5:
        print("You are underweight.")
    elif bmi_value >= 18.5 and bmi_value <= 25:
        print("You are normal.")
    elif bmi_value >= 25 and bmi_value <= 30:
        print("You are overweight.")
    else:
        print("You are obese.")
    print()
    
    again = input("Do you want to math again?(y/n) ").lower()
    while again != "n" and again != "y":
        again = input("Please answer yes or no!(y/n) ").lower()
        print()
                
    if again == "n":
        bmi_calculate = 0
        print()
        print("Bye!!!")
        print()
