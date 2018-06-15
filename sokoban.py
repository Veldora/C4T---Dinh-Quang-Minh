import random

play = 1

map1 = {
    "size_x": 5,
    "size_y": 5
}

player = {
        "x": 100,
        "y": 100
}

undo_player = dict(player)

player["x"] = random.randrange(0, 5)
player["y"] = random.randrange(0, 5)

boxes = [
    {
        "x": 100,
        "y": 100
    },
    {
        "x": 100,
        "y": 100
    },
    {
        "x": 100,
        "y": 100
    }
]

undo_boxes = [
    {
        "x": 100,
        "y": 100
    },
    {
        "x": 100,
        "y": 100
    },
    {
        "x": 100,
        "y": 100
    }
]

for i in range(3):
    require_same = 1

    while require_same == 1:
        bix = random.randrange(1, 4)
        biy = random.randrange(1, 4)
        require_same = 0
        
        for box in range(len(boxes)):
            if boxes[box]["x"] == bix and boxes[box]["y"] == biy:
                require_same = 1
        if bix == player["x"] and biy == player["y"]:
            require_same = 1

    boxes[i]["x"] = bix
    boxes[i]["y"] = biy

destinations = [
    {
        "x": 100,
        "y": 100
    },
    {
        "x": 100,
        "y": 100
    },
    {
        "x": 100,
        "y": 100
    }
]

undo_destinations = [
    {
        "x": 100,
        "y": 100
    },
    {
        "x": 100,
        "y": 100
    },
    {
        "x": 100,
        "y": 100
    }
]

wall = []

for i in range(3):
    require_same = 1

    while require_same == 1:
        dix = random.randrange(0, 5)
        diy = random.randrange(0, 5)
        require_same = 0

        for destination in range(len(destinations)):
            if destinations[destination]["x"] == dix and destinations[destination]["y"] == diy:
                require_same = 1
        for box in range(len(boxes)):
            if boxes[box]["x"] == dix and boxes[box]["y"] == diy:
                require_same = 1
        if dix == player["x"] and diy == player["y"]:
            require_same = 1

    destinations[i]["x"] = dix
    destinations[i]["y"] = diy

print()

level = 1
level_print = 1

print("SOKOBAN")
print()
print("Player:      P")
print("Box:         B")
print("Destination: D")
print("Wall:        |")
print()
print("READY!")
print()
print("3")
print()
print("2")
print()
print("1")
print()
print("START!")
print()

while play == 1:
    if level_print == 1:
        print("LEVEL " + str(level) + ":")
        level_print = 0
    print()
    move_able = 1
    for y in range(map1["size_y"]):
        for x in range(map1["size_x"]):
            box_is_here = False
            player_is_here = False
            destinations_is_here = False
            wall_is_here = False
            for box in range(len(boxes)):
                if boxes[box]["x"] == x and boxes[box]["y"] == y:
                    box_is_here = True
            for destination in range(len(destinations)):
                if destinations[destination]["x"] == x and destinations[destination]["y"] == y:
                    destinations_is_here = True
            for walls in range(len(wall)):
                if wall[walls]["x"] == x and wall[walls]["y"] == y:
                    wall_is_here = True
            if x == player["x"] and y == player["y"]:
                player_is_here = True

            if box_is_here:
                print("B", end=" ")
            elif player_is_here:
                print("P", end=" ")
            elif destinations_is_here:
                print("D", end=" ")
            elif wall_is_here:
                print("|", end=" ")
            
            else:
                print("-", end=" ")
        print()

    
    destination_require_list = []
    for destination in range(len(destinations)):
        des = 0
        for box in range(len(boxes)):
            if destinations[destination] == boxes[box]:
                destination_require_list.append(1)
                des = 1
        if des == 0:
            destination_require_list.append(0)

    destination_require = 1
    for d in range(len(destination_require_list)):
        if destination_require_list[d] == 0:
            destination_require = 0
    
    if destination_require == 1:
        print()
        

        if level != 5:
            print("Congrats, you`ve just pass level " + str(level) + "!")
            play_again = input("Next level?(y/n) ").lower()
            
            while play_again != "n" and play_again != "y":
                play_again = input("Please answer yes or no!(y/n)").lower()
                print()

            if play_again == "n":
                play = 0
                print()
                print("GAME OVER!!!")
                print()
                move_able = 0
                move = "legvhhlgehlehlayerghlriehgalehgelirghalehgeligh877q07re987geyrgyeg"
                
            elif play_again == "y":
                px = 100
                py = 100
                print()
                require = 1
                move_able = 0

                map1["size_x"] += 1
                map1["size_y"] += 1
                level += 1
                level_print = 1
                
                player = {
                        "x": 100,
                        "y": 100
                }

                undo_player = dict(player)

                player["x"] = random.randrange(0, 4 + level)
                player["y"] = random.randrange(0, 4 + level)

                boxes = []
                for i in range(level + 2):
                    boxes.append({"x": 100, "y": 100})

                undo_boxes = []
                for i in range(level + 2):
                    undo_boxes.append({"x": 100, "y": 100})

                for i in range(level + 2):
                    require_same = 1

                    while require_same == 1:
                        bix = random.randrange(1, 3 + level)
                        biy = random.randrange(1, 3 + level)
                        require_same = 0
                        
                        for box in range(len(boxes)):
                            if boxes[box]["x"] == bix and boxes[box]["y"] == biy:
                                require_same = 1
                        if bix == player["x"] and biy == player["y"]:
                            require_same = 1

                    boxes[i]["x"] = bix
                    boxes[i]["y"] = biy

                destinations = []
                for i in range(level + 2):
                    destinations.append({"x": 100, "y": 100})

                undo_destinations = []
                for i in range(level + 2):
                    undo_destinations.append({"x": 100, "y": 100})

                for i in range(level + 2):
                    require_same = 1

                    while require_same == 1:
                        dix = random.randrange(0, 4 + level)
                        diy = random.randrange(0, 4 + level)
                        require_same = 0

                        for destination in range(len(destinations)):
                            if destinations[destination]["x"] == dix and destinations[destination]["y"] == diy:
                                require_same = 1
                        for box in range(len(boxes)):
                            if boxes[box]["x"] == dix and boxes[box]["y"] == diy:
                                require_same = 1
                        if dix == player["x"] and diy == player["y"]:
                            require_same = 1

                    destinations[i]["x"] = dix
                    destinations[i]["y"] = diy
                    
                wall = []
                for i in range(level):
                    wall.append({"x": 100, "y": 100})
                for i in range(level):
                    require_same = 1

                    while require_same == 1:
                        dix = random.randrange(0, 4 + level)
                        diy = random.randrange(0, 4 + level)
                        require_same = 0

                        for destination in range(len(destinations)):
                            if destinations[destination]["x"] == dix and destinations[destination]["y"] == diy:
                                require_same = 1
                        for box in range(len(boxes)):
                            if boxes[box]["x"] == dix and boxes[box]["y"] == diy:
                                require_same = 1
                        for walls in range(len(wall)):
                            if wall[walls]["x"] == dix and wall[walls]["y"] == diy:
                                require_same = 1
                        if dix == player["x"] and diy == player["y"]:
                            require_same = 1

                    wall[i]["x"] = dix
                    wall[i]["y"] = diy
            
        else:
            print("Congrats, you`ve just won the game!!!")
            play_again = input("Do you want to play again?(y/n) ").lower()
            
            while play_again != "n" and play_again != "y":
                play_again = input("Please answer yes or no!(y/n)").lower()
                print()

            if play_again == "n":
                play = 0
                print()
                print("Bye!!!")
                print()
                move_able = 0
                move = "legvhhlgehlehlayerghlriehgalehgelirghalehgeligh877q07re987geyrgyeg"
                
            elif play_again == "y":
                level_print = 1
                px = 100
                py = 100
                print()
                require = 1
                move_able = 0

                map1["size_x"] = 5
                map1["size_y"] = 5
                level = 1
                
                player = {
                        "x": 100,
                        "y": 100
                }

                undo_player = dict(player)

                player["x"] = random.randrange(0, 5)
                player["y"] = random.randrange(0, 5)

                boxes = [
                    {
                        "x": 100,
                        "y": 100
                    },
                    {
                        "x": 100,
                        "y": 100
                    },
                    {
                        "x": 100,
                        "y": 100
                    }
                ]

                undo_boxes = [
                    {
                        "x": 100,
                        "y": 100
                    },
                    {
                        "x": 100,
                        "y": 100
                    },
                    {
                        "x": 100,
                        "y": 100
                    }
                ]

                for i in range(3):
                    require_same = 1

                    while require_same == 1:
                        bix = random.randrange(1, 4)
                        biy = random.randrange(1, 4)
                        require_same = 0
                        
                        for box in range(len(boxes)):
                            if boxes[box]["x"] == bix and boxes[box]["y"] == biy:
                                require_same = 1
                        if bix == player["x"] and biy == player["y"]:
                            require_same = 1

                    boxes[i]["x"] = bix
                    boxes[i]["y"] = biy

                destinations = [
                    {
                        "x": 100,
                        "y": 100
                    },
                    {
                        "x": 100,
                        "y": 100
                    },
                    {
                        "x": 100,
                        "y": 100
                    }
                ]

                undo_destinations = [
                    {
                        "x": 100,
                        "y": 100
                    },
                    {
                        "x": 100,
                        "y": 100
                    },
                    {
                        "x": 100,
                        "y": 100
                    }
                ]

                for i in range(3):
                    require_same = 1

                    while require_same == 1:
                        dix = random.randrange(0, 5)
                        diy = random.randrange(0, 5)
                        require_same = 0

                        for destination in range(len(destinations)):
                            if destinations[destination]["x"] == dix and destinations[destination]["y"] == diy:
                                require_same = 1
                        for box in range(len(boxes)):
                            if boxes[box]["x"] == dix and boxes[box]["y"] == diy:
                                require_same = 1
                        if dix == player["x"] and diy == player["y"]:
                            require_same = 1

                    destinations[i]["x"] = dix
                    destinations[i]["y"] = diy
                wall = []
            

    if move_able == 1:
        move = input("Your move(W, A, S, D)? Or you can enter P to play again, U to undo! ").lower()
    print()
    require = 0

    while move != 'w' and move != "s" and move != "a" and move != "d" and move != "p" and move != "u" and move != "legvhhlgehlehlayerghlriehgalehgelirghalehgeligh877q07re987geyrgyeg":
        print()
        move = input("Please enter W, A, S, D, P or U!").lower()
        print()

    if move == "w":
        py = player["y"] - 1
        px = player["x"]
    elif move == "s":
        py = player["y"] + 1
        px = player["x"]
    elif move == "a":
        px = player["x"] - 1
        py = player["y"]
    elif move == "d":
        px = player["x"] + 1
        py = player["y"]
    elif move == "u":
        px = 100
        py = 100
        print()
        require = 1
        move_able = 0
        if undo_player["x"] != 100:
            player = dict(undo_player)
            for box in range(len(boxes)):
                boxes[box] = dict(undo_boxes[box])
            for destination in range(len(destinations)):
                destinations[destination] = dict(undo_destinations[destination])
        
    elif move == "p":
        level_print = 1
        px = 100
        py = 100
        print()
        require = 1
        move_able = 0

        map1["size_x"] = 5
        map1["size_y"] = 5
        level = 1
            
        player = {
                "x": 100,
                "y": 100
        }

        undo_player = dict(player)

        player["x"] = random.randrange(0, 5)
        player["y"] = random.randrange(0, 5)

        boxes = [
            {
                "x": 100,
                "y": 100
            },
            {
                "x": 100,
                "y": 100
            },
            {
                "x": 100,
                "y": 100
            }
        ]

        undo_boxes = [
            {
                "x": 100,
                "y": 100
            },
            {
                "x": 100,
                "y": 100
            },
            {
                "x": 100,
                "y": 100
            }
        ]

        for i in range(3):
            require_same = 1

            while require_same == 1:
                bix = random.randrange(1, 4)
                biy = random.randrange(1, 4)
                require_same = 0
                    
                for box in range(len(boxes)):
                    if boxes[box]["x"] == bix and boxes[box]["y"] == biy:
                        require_same = 1
                if bix == player["x"] and biy == player["y"]:
                    require_same = 1

            boxes[i]["x"] = bix
            boxes[i]["y"] = biy

        destinations = [
            {
                "x": 100,
                "y": 100
            },
            {
                "x": 100,
                "y": 100
            },
            {
                "x": 100,
                "y": 100
            }
        ]

        undo_destinations = [
            {
                "x": 100,
                "y": 100
            },
            {
                "x": 100,
                "y": 100
            },
            {
                "x": 100,
                "y": 100
            }
        ]

        for i in range(3):
            require_same = 1

            while require_same == 1:
                dix = random.randrange(0, 5)
                diy = random.randrange(0, 5)
                require_same = 0

                for destination in range(len(destinations)):
                    if destinations[destination]["x"] == dix and destinations[destination]["y"] == diy:
                        require_same = 1
                for box in range(len(boxes)):
                    if boxes[box]["x"] == dix and boxes[box]["y"] == diy:
                        require_same = 1
                if dix == player["x"] and diy == player["y"]:
                    require_same = 1

            destinations[i]["x"] = dix
            destinations[i]["y"] = diy
        wall = []
            
    if px != 100 or py != 100:
##        for destination in range(len(destinations)):
##            if destinations[destination]["x"] == px and destinations[destination]["y"] == py:
##                require = 1

        for walls in range(len(wall)):
            if wall[walls]["x"] == px and wall[walls]["y"] == py:
                require = 1

        if px < 0 or py < 0 or px >= 4 + level or py >= 4 + level:
            print()
            print("You are not allowed to get out of the map!")
            print()
            require = 1

        player_hit_box = 100
        for box in range(len(boxes)):
            if boxes[box]["x"] == px and boxes[box]["y"] == py:
                player_hit_box = box

        bx = 100
        by = 100

        if player_hit_box != 100:
            if move == "w":
                by = boxes[player_hit_box]["y"] - 1
                bx = boxes[player_hit_box]["x"]
            elif move == "s":
                by = boxes[player_hit_box]["y"] + 1
                bx = boxes[player_hit_box]["x"]
            elif move == "a":
                bx = boxes[player_hit_box]["x"] - 1
                by = boxes[player_hit_box]["y"]
            elif move == "d":
                bx = boxes[player_hit_box]["x"] + 1
                by = boxes[player_hit_box]["y"]

        if bx != 100 or by != 100:
            if bx < 0 or by < 0 or bx >= 4 + level or by >= 4 + level:
                print()
                print("You are not allowed to move the box out of the map!")
                print()
                require = 1
            for walls in range(len(wall)):
                if wall[walls]["x"] == bx and wall[walls]["y"] == by:
                    require = 1
            for destination in range(len(destinations)):
                if destinations[destination]["x"] == bx and destinations[destination]["y"] == by:
                    undo_player = dict(player)
                    for box1 in range(len(boxes)):
                        undo_boxes[box1] = dict(boxes[box1])
                    for destination1 in range(len(destinations)):
                        undo_destinations[destination1] = dict(destinations[destination1])
                    
                    boxes[player_hit_box]["y"] = by
                    boxes[player_hit_box]["x"] = bx
                    player["y"] = py
                    player["x"] = px
##                    destinations[destination]["x"] = 100
##                    destinations[destination]["y"] = 100
                    require = 1
            for box in range(len(boxes)):
                if boxes[box]["x"] == bx and boxes[box]["y"] == by:

                    require = 1





    if require == 0:
        undo_player = dict(player)
        for box in range(len(boxes)):
            undo_boxes[box] = dict(boxes[box])
        for destination in range(len(destinations)):
            undo_destinations[destination] = dict(destinations[destination])
        player["y"] = py
        player["x"] = px
        if player_hit_box != 100:
            boxes[player_hit_box]["y"] = by
            boxes[player_hit_box]["x"] = bx
