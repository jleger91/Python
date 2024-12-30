
#rooms dictionary
rooms = {
    'Main Hall': {'N': 'Dining Room', 'E': 'Library', 'S': 'Bathroom'},
    'Dining Room': {'E': 'Kitchen', 'S': 'Main Hall'},
    'Kitchen': {'W': 'Dining Room', 'S': 'Library'},
    'Library': {'N': 'Kitchen', 'S': 'Bedroom', 'E': 'Cellar', 'W': 'Main Hall'},
    'Bedroom': {'N': 'Library', 'W': 'Bathroom'},
    'Bathroom': {'N': 'Main Hall', 'E': 'Bedroom'},
    'Cellar': {}
}
items = {
    'Main Hall': {'Item': 'none'},
    'Dining Room': {'Item': 'Helm'},
    'Kitchen': {'Item': 'Shield'},
    'Library': {'Item': 'Sword'},
    'Bedroom': {'Item': 'Armor'},
    'Bathroom': {'Item': 'Potion'},
    'Cellar': {'Item': 'none'}
}

def room_jump(direction, current_room, rooms):
    # set current room using dictionary
    new_room = rooms[current_room][direction]
    #return updated room
    return new_room

def print_instructions(current_room, dir_list, items, inventory):
    print('current room is:', current_room)
    print('You can go:', dir_list)
    print('Items in room:', items[current_room]['Item'])
    print('Your inventory:', inventory)
    print('You can type the direction or the name of the item')

def validate_input(dir_list, items, current_room):
    user_input = input()
    if ((user_input not in dir_list) and
            (user_input != items[current_room]['Item'])):
        print('Invalid user input')
        return False, user_input
    return True, user_input

def get_item(user_input, items, current_room):
    # if user gets item
    if (user_input == items[current_room]['Item']):
        # there is an item not called 'none'
        if (items[current_room]['Item'] != 'none'):
            inventory.append(items[current_room]['Item'])
            items[current_room].pop('Item')
            items[current_room]['Item'] = 'none'
            return False
        else:
            print('invalid item')
            return False
    return True

def vyril(inventory):
    # dealing with Vyril
    if (len(inventory) < 5):
        print('You encounter Vyril unprepared!')
        print('He stabs you and laughs!')
        print('You have died!')
        return False
    elif (len(inventory) == 5):
        print('You encounter Vyril fully prepared')
        print('You slash at him with your sword')
        print('You have defeated Vyril and found treasure')
        print('You are victorious!')
        return False
    return True

#initial variables
current_room = 'Main Hall'
self = 0
inventory = []
game_running = True

#main game loop
while (game_running):
    # list directions you can move in
    dir_list = list(rooms[current_room].keys())
    #list item in the room
    item_list = list(items[current_room].keys())
    # print room-entry instructions:
    print_instructions(current_room, dir_list, items, inventory)

    # get valid user input
    is_valid, user_input = validate_input(dir_list, items, current_room)
    if (not is_valid):
        continue

    #attempt to get item
    item_gotten = get_item(user_input, items, current_room)
    if (not item_gotten):
        continue

    #attempt to jump room
    current_room = room_jump(user_input, current_room, rooms)

    #attempt to handle Vyril
    if (current_room == 'Cellar'):
        game_running = vyril(inventory)

print('The End!')