
from adventurelib import *

Room.items = Bag()

current_room = starting_room = Room("""
you wake up in a room with two doors one says elf and the other says dwarf

west to go into the dwarf door, east to go into to the elf door
""")

magic_forest = starting_room.north = Room("""
You are in a enchanted forest where magic grows wildly.
""")

elf_room1 = starting_room.east = Room("""
you transform into a elf
""")

dwarf_room1 = starting_room.west = Room("""
you transform into a dwarf
""")

dwarf_room2 = dwarf_room1.south = Room("""
you are in a great hall in a abanded castle
""")

elf_room2 = elf_room1.south = Room("""
you are in a great hall in a abanded castle
""")

dwarf_room3 = dwarf_room2.west = Room("""
you are in a bedroom
""")

elf_room3 = elf_room2.east = Room("""
you are on a sidewalkk
""") 

dwarf_room4 = dwarf_room3.south = Room("""
you are in a game room
""")

elf_room4 = elf_room3.south = Room("""
you are in a house
""")

dwarf_room5 = dwarf_room4.south = Room("""
you are on the sidewalk that the wizard owns
""")

elf_room5 = elf_room4.south = Room("""
you are ambushed by goblins (you thought) they just want to scare you and they join your side!
""")

dwarf_room6 = dwarf_room5.south = Room("""
a wizard says "i'm suprized you made it this far i'll let you just go for this one time" and you go in
""")

elf_room6 = elf_room5.south = Room("""
you spot a wizard and he says"good job goblins you may go now" "ok" says a goblin you go in and hide to ambush the dwarves
""")

dwarf_room7 = dwarf_room6.north = Room("""
the elves ambush you! but you win the fight you take the gem but a dragon appears and melts you!







===============================================THE END===============================================

                                             (or is it?)
""")

elf_room7 = elf_room6.north = Room("""
you ambush the dwarves but lose the fight!

================================================THE END==============================================

                                              (or is it?)
""")

magic_forest2 = magic_forest.north = Room("""
you see a magic cave
""")

magic_forest3 = magic_forest2.north = Room("""
you take the real gem of power

===============================================YOU WIN=================================================
""")


sewer_room1 = starting_room.south = Room("""
you see the gem but know not to take it
""")

sewer_room2 = sewer_room1.north = Room("""
you spot a secret entrance you go in to it and you get armour a sheild and a sword
""")

sewer_room3 = sewer_room2.south = Room("""
a dragon is through the secret passage way
""")

sewer_room4 = sewer_room3.north = Room("""
you go to the dragon and kill it and you see a portal you go into it
""")

sewer_room5 = sewer_room4.north = Room("""
you tellaport to the gem room you take the real gem of power

===============================================YOU WIN=================================================
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
        if room == magic_forest:
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