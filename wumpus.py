import random


class Maze(object):

    def __init__(self, Rooms):
        self.Rooms = Rooms

    def describe_room(self, room_num):
        return self.Rooms[room_num].desc + "Your adjacent rooms are: " + str(self.Rooms[room_num].rooms_list)


class Movable(Maze):

    def randomly_place(self, maze, off_limit_rooms=None):
        self.maze = maze.Rooms
        self.off_limit_rooms = off_limit_rooms
        if off_limit_rooms:
            self.location = random.choice(
                [x for x in [0, 1, 2, 3, 4, 5] if x not in self.off_limit_rooms])
        else:
            self.location = random.choice([0, 1, 2, 3, 4, 5])

    def is_near(self, mov_obj, maze):
        if self.location in maze.Rooms[mov_obj.location].rooms_list:
            return True

    def move_to(self, target):
        self.location = target


class Room(Maze):

    def __init__(self, room_num, desc, rooms_list):
        self.room_num = room_num
        self.desc = desc
        self.rooms_list = rooms_list


class Monster(Movable):

    def __init__(self, mon_name, start_room=0):
        self.mon_name = mon_name
        self.start_room = start_room
        self.location = start_room


class Command(object):

    def __init__(self, command_type, target):
        if command_type == "go to":
            self.command_type = "move"
        else:
            self.command_type = "shoot"
        self.target = target


class Player(Movable):

    def __init__(self, num_darts=1, start_room=0):
        self.num_darts = num_darts
        self.start_room = start_room
        self.location = start_room

    def shoot(self):
        if self.num_darts == 0:
            return False
        else:
            self.num_darts -= 1
            return True

    def get_command(self, maze):
        while(True):
            command = input().split()
            command_type = " ".join(command[:2]).lower()
            if command[2].isnumeric():
                target = int(command[2])
            else:
                print("Please enter a command with a  valid room number:")
                continue
            if "go to" in command_type or "shoot into" in command_type:
                if target in maze.Rooms[self.location].rooms_list:
                    return Command(command_type, target)
                else:
                    print("Please enter an adjacent room number.")
                    continue
            else:
                print(
                    "Please enter a valid command of the format  \"go to <adjacent room>\" or \"shoot into  < adjacent room>\"")
