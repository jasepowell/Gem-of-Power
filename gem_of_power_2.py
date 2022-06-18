from lib.engine import *

Room.items = Bag()

current_room = starting_room = Room("""
you wake up in a room with two doors, one says elf and the

other says dwarf.

west to  go into the dwarf door, east to go into the elf door
""")

magic_cave = starting_room.south = Room("""
You are in a enchanted cave where magic grows wildly.
""")

magic_cave1 = magic_cave.south = Room("""
you find a secret tunnle and you go in
""")

magic_cave2 = magic_cave1.south = Room("""
you find your self under the castle in the gem room.

you take the gem and use it's power to go home

=========================YOU WIN============================
""")

gem_room = starting_room.north = Room("""
you walk into the gem room you see armour, sheilds ,and swords

you take them and get the gem and think about using it's power

but instead you just take it and go through a secret passage

way.
""")
gem_room1 = gem_room.north = Room("""
you see a giant snake you fight it and you kill it.

============================YOU WIN============================
""")

dwarf_room = starting_room.west = Room("""

""")




























"""DONT CHANGE ANYTHING BELOW HERE."""

inventory = Bag()


@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        say('You go %s.' % direction)
        look()
        if room == magic_cave:
            set_context('magic_aura')
        else:
            set_context('default')
    else:
        say('A mysterious force is preventing you from moving %s' % direction)


@when('take ITEM')
def take(item):
    obj = current_room.items.take(item)
    if obj:
        say('You pick up the %s.' % obj)
        inventory.add(obj)
    else:
        say('There is no %s here.' % item)


@when('drop THING')
def drop(thing):
    obj = inventory.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    else:
        say('You drop the %s.' % obj)
        current_room.items.add(obj)


@when('look')
def look():
    say(current_room)
    if current_room.items:
        for i in current_room.items:
            say('A %s is here.' % i)


@when('inventory')
def show_inventory():
    say('You have:')
    for thing in inventory:
        say(thing)

@when('cast', context='magic_aura', magic=None)
@when('cast MAGIC', context='magic_aura')
def cast(magic):
    if magic == None:
        say("Which magic you would like to spell?")
    elif magic == 'fireball':
        say("A flaming Fireball shoots form your hands!")

look()
start()