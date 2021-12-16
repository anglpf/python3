from sys import exit
from random import randint
from textwrap import dedent # This helps us to write our room descriptions using """ strings. Without it, """ strings fail because they're indented on the screen the same level as in the Python code.

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):

    quips = [
        "You are dead. Nice one.",
        "Oh dear, that's not what's supposed to happen."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print("You are in the central corridor.")
        print("...")
        print("There is a Gothon standing guard, watching you. It has a loaded gun pointed in your direction.")
        print("...")
        print("You'd better make it happy.")

        action = input("> ")

        if action == "shoot" or action == "shoot the Gothon":
            print("You draw your weapon...")
            print("...but the Gothon's aim is already locked onto you.")
            print("It shoots. It hits.")
            return 'death'

        elif action == "dodge":
            print("The Gothon shoots!")
            print("Its laser narrowly misses your head... you duck behind some cover.")
            print("The corridor quietens.")
            return 'central_corridor'

        elif action == "tell a joke":
            print("")
            return 'laser_weapon_armory'

        else:
            print("The Gothon continues to stare you down.")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print("You are in the laser-weapon armory.")
        print("...")
        print("It looks like there's something on the ground over there.")
        print("...")
        print("It's a neutrino bomb. You pick it up and put it in your backpack.")

class TheBridge(Scene):

    def enter(self):
        print("You are in the bridge.")
        print("...")
        print("There are lots of Gothons in here.")
        print("...")
        print("You'd better find a way through.")

class EscapePod(Scene):

    def enter(self):
        print("You are in the escape pod.")

class Finished(Scene):

    def enter(self):
        print("You successfully defeated the Gothons.")
        print("Nice one!")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
