
done = False

room_list = []

room = ["0 You are in the Bedroom 2. The guest can sleep here. There is a room to the east",None,1,None,None]     #0
room_list.append(room)
room = ["1 You are in the South Hall. A big Hall in the south of the buildung. There are rooms to the north east and west",4,2,None,0]  #1
room_list.append(room)
room = ["2 You are in the Dining Room. There is a room to the north and west",3,None,None,1] #2
room_list.append(room)
room = ["3 You are in the Kitchen. You may find something good to eat here. There is a room to the south",None,None,2,None] #3
room_list.append(room)
room = ["4 You are in the Great Hall. A even bigger Hall than the South Hall. There are rooms to the north and south",6,None,1,None] #4
room_list.append(room)
room = ["5 You are in the Bedroom 1. The Owner sleeps here. There is a room to the east.",None,6,None,None] #5
room_list.append(room)
room = ["6 You are in the Office. There are rooms to the north, south and west. Whats that? It looks like there is a door behind the bookshelf to the east",8,7,4,5] #6
room_list.append(room)
room = ["7 You found a secret room. Looks like someone was hiding here. There is a room to the west",None,None,None,6]  #7
room_list.append(room)
room = ["8 You are on the balcony. There is a room to the south",None,None,6,None]  #8
room_list.append(room)

current_room = 0

while not done:

    print(room_list[current_room][0])
    user=input("What direction do you want to go? Type (N)orth, (E)ast, (S)outh or (W)est ")
    
    #go to north
    if user.upper()=="N":
        next_room = room_list[current_room][1]

        if next_room == None:
            print()
            print("You can't go that way.")
        else:
            current_room=next_room
    #go to east
    elif user.upper()=="E" :
        next_room=room_list[current_room][2]
        if next_room==None:
            print("You can't go that way.")
        else:
            current_room=next_room
    #go to south
    elif user.upper()=="S" :
        next_room=room_list[current_room][3]
        if next_room==None:
            print("You can't go that way.")
        else:
            current_room=next_room
    #go to west
    elif user.upper()=="W" :
        next_room=room_list[current_room][4]
        if next_room==None:
            print("You can't go that way.")
        else:
            current_room=next_room
    #Quit
    elif user.upper()=="Q":
       done=True
    #Wrong input
    else:
        print()
        print("Cant handle the input")


