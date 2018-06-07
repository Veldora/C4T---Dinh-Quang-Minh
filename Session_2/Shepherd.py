print("2.1")
sizes = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hiep and there are my ship sizes:", end = " ")
print(*sizes, sep = ", ")

print()

print("2.2")
print("Now my biggest sheep has size", max(sizes),"let's shear it")

print()

print("2.3")
sizes[sizes.index(max(sizes))] = 8
print("After shearing, here is my flock:", end = " ")
print(*sizes, sep = ", ")

print()

print("2.4")
sizes = [size + 50 for size in sizes]
print("One month has passed, now here is my flock:", end = " ")
print(*sizes, sep = ", ")

print()

print("2.5 and 2.6")
shear = 1
while shear == 1:
    require = 1

    while require == 1:
        try:
            month = int(input("How many months do you want to be a shepherd:))? "))
            require = 0
        except ValueError:
            print()
            print("Int please!!!")
            require = 1
            continue
        if month < 1:
            print()
            print(">0 please!!!")
            require = 1

    sizes = [5, 7, 300, 90, 24, 50, 75]
    print("Hello, my name is Hiep and there are my ship sizes:", end = " ")
    print(*sizes, sep = ", ")
    print()
    print("Now my biggest sheep has size", max(sizes),"let's shear it")
    print()
    sizes[sizes.index(max(sizes))] = 8
    print("After shearing, here is my flock:", end = " ")
    print(*sizes, sep = ", ")
    print()
    print()

    
    for i in range(month):
        if i == month - 1:
            print("MONTH", i + 1, ":")
            sizes = [size + 50 for size in sizes]
            print("One month has passed, now here is my flock:", end = " ")
            print(*sizes, sep = ", ")
            print()
            print()
            
        else:
            print("MONTH", i + 1, ":")
            sizes = [size + 50 for size in sizes]
            print("One month has passed, now here is my flock:", end = " ")
            print(*sizes, sep = ", ")
            print()
            print("Now my biggest sheep has size", max(sizes),"let's shear it")
            print()
            sizes[sizes.index(max(sizes))] = 8
            print("After shearing, here is my flock:", end = " ")
            print(*sizes, sep = ", ")
            print()
            print()

    print("My flock has size in total:", sum(sizes))
    print("I would get", sum(sizes), "* 2$ =", sum(sizes) * 2, "$")

    again = input("Do you want to be a shepherd again?(y/n) ").lower()
    while again != "n" and again != "y":
        again = input("Please answer yes or no!(y/n) ").lower()
        print()
                
    if again == "n":
        shear = 0
        print()
        print("Bye!!!")
        print()
