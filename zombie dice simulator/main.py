import zombiedice
import pprint
import random


class OneShotgunBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        while shotguns < 2:
            roll = zombiedice.roll()
            shotguns += roll['shotgun']


class FotstepsColorBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        while shotguns <= 2:
            roll = zombiedice.roll()
            shotguns += roll['shotgun']
            dierolls = [rl.color for rl in roll['rolls'] if rl.icon == "footsteps"]
            dierolls = {'red': dierolls.count("red"), 'yellow': dierolls.count("yellow")}
            if shotguns == 0 and dierolls['red'] <= 2 and dierolls['yellow'] == 0:
                continue
            if shotguns == 1 and dierolls['red'] <= 1:
                continue
            if shotguns == 2 and dierolls['red'] == 0 and dierolls['yellow'] <= 2:
                continue
            break


class RerollPrecentageBot:
    def __init__(self, name, percentage):
        self.name = name
        self.percentage = percentage

    def turn(self, gameState):
        zombiedice.roll()
        while True:
            if random.randrange(100) < self.percentage:
                zombiedice.roll()
                continue
            break


class SimpleBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        zombiedice.roll()

class LeadingBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        while shotguns <= 2 or gameState['SCORES'][self.name] != max(gameState['SCORES'].values()):
            roll = zombiedice.roll()
            shotguns += roll['shotgun']
            dierolls = [rl.color for rl in roll['rolls'] if rl.icon == "footsteps"]
            dierolls = {'red': dierolls.count("red"), 'yellow': dierolls.count("yellow")}
            if shotguns == 0 and dierolls['red'] <= 2 and dierolls['yellow'] == 0:
                continue
            if shotguns == 1 and dierolls['red'] <= 1:
                continue
            if shotguns == 2 and dierolls['red'] == 0 and dierolls['yellow'] <= 2:
                continue
            break




zombie = (
    LeadingBot("LeadingBot"),
    SimpleBot("SimpleBot"),
    RerollPrecentageBot("bot 50%", 50),
    RerollPrecentageBot("bot 25%", 25),
    RerollPrecentageBot("bot 75%", 75),
    # OneShotgunBot("OneShotgunBot"),
    FotstepsColorBot("FootstepsColorBot")
)

zombiedice.runWebGui(zombies=zombie, numGames=1)
