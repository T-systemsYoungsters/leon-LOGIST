
done = False

room_list = []

room = ["You are in the Bedroom 2. The guest can sleep here. There is a room to the east",None,1,None,None]
room_list.append(room)
room = ["You are in the South Hall. A big Hall in the south of the buildung. There are rooms to the north east and west",4,2,None,0]
room_list.append(room)
room = ["You are in the Dining Room. There is a room to the north and west",3,None,None,1]
room_list.append(room)
room = ["You are in the Kitchen. You may find something good to eat here. There is a room to the south",None,None,2,None]
room_list.append(room)
room = ["You are in the Great Hall. A even bigger Hall than the South Hall. There are rooms to the north and south",6,None,1,None]
room_list.append(room)
room = ["You are in the Office. There are rooms to the north, south and west. Whats that? It looks like there is a door behind the bookshelf to the east",8,7,4,5]
room_list.append(room)
room = ["You are in the Bedroom 1. The Owner sleeps here. There is a room to the east.",None,6,None,None]
room_list.append(room)
room = ["You are on the balcony. There is a room to the south",None,None,6,None]
room_list.append(room)
room = ["You found a secret room. Looks like someone was hiding here. There is a room to the west",None,None,6,None]
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


