from flask import session
from random import random, uniform

# Example init for player: Stats('playerStats')
# Example init for random mob: Stats(None, {'health': 10,'attack': 10, 'agility': 10, 'luck': 10})
class Stats:
    def __init__(self, storageKey = None, defaultStats = None):
        if defaultStats:
            self.stats = defaultStats
        else:
            self.storageKey = storageKey
            self.load()

    # Get stats from storage or instatiate them if they don't exist
    def load(self):
        stats = session.get(self.storageKey)
        if stats:
            self.stats = stats
        else:
            self.stats = {
                'health': 10,
                'attack': 10,
                'agility': 10,
                'luck': 10
            }
            self.save()

    def save(self):
        if self.storageKey:
            session[self.storageKey] = self.stats

    def rollDodge(self, enemyAgility = 10):
        enemyRand = uniform(1.0, 1.5)
        selfRand = uniform(0.5, 1.5)

        print('enemyDodge:', enemyRand)
        print('self dodge:', selfRand)

        return (selfRand * self.stats['agility']) > (enemyRand * enemyAgility)

    def rollEscape(self, enemyAgility = 10):
        return self.rollDodge(enemyAgility)

    def rollCrit(self):
        rand = random()
        odds = self.stats['luck'] / 100
        return odds >= rand

    def rollAttack(self):
        # Get random multiplier
        mult = uniform(0.8, 1.2)
        damage = self.stats['attack'] / 4 * mult

        if self.rollCrit():
            damage *= 1.5

        return round(damage)

    def __getitem__(self, key) :
        if key in self.stats:
            return self.stats[key]
        else:
            return None

    def __setitem__(self, key, value):
        self.stats[key] = value
        self.save()