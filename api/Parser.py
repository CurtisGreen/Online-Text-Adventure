from Player import Player
from Enemy import Enemy

class Parser():
    def parse(self, input):
        print('parsing')
        inputArr = self.cleanInput(input)

        response = self.checkMove(inputArr)
        if (response != None):
            return response
        
        response = self.checkAttack(inputArr)
        if (response != None):
            return response
        
        return 'Invalid command'

    # Clean up and simplify input before parsing ('move to the west' -> ['move', 'west'])
    def cleanInput(self, input):
        inputArr = input.lower().split(' ')
        for item in ['a', 'an', 'the', 'to']:
            while item in inputArr: inputArr.remove(item)
        return inputArr


    # Check if they are trying to move locations (up, north, etc.)
    def checkMove(self, inputArr):
        # 1 word move (Ex: 'up')
        if len(inputArr) == 1 and self.verifyDirection(inputArr[0]):
            return 'Moved ' + inputArr[0]
        # 2 word move (Ex: 'move up')
        elif len(inputArr) == 2 and self.verifyMove(inputArr[0]) and self.verifyDirection(inputArr[1]):
            return 'Moved ' + inputArr[1]
        else:
            return None

    def verifyMove(self, action):
        actions = {'move', 'go', 'run'}
        return (action in actions)
    
    def verifyDirection(self, dir):
        directions = {'up', 'down', 'left', 'right', 'north', 'south', 'east', 'west', 'forwards', 'backwards'}
        return (dir in directions)


    def checkAttack(self, inputArr):
        actions = {'attack', 'hit', 'kill'}
        # 1 word action ('attack'), attack current target if it exists
        if len(inputArr) == 1 and inputArr[0] in actions:
            return self.fightEnemy()
        # 2 word action ('attack goblin'), attack if that target exists
        elif len(inputArr) == 2 and inputArr[0] in actions:
            return 'There is no ' + inputArr[1] + ' to attack here'
        else:
            return None

    # Temp fighting logic
    def fightEnemy(self):
        outString = ''
        player = Player()
        enemy = Enemy('goblin')

        # Player's turn
        # Check enemy dodge
        enemyDodge = enemy.stats.rollDodge(player.stats['agility'])
        if enemyDodge:
            outString += 'The enemy dodged.\n'
        # Do damage
        else:
            damage = player.stats.rollAttack()
            enemy.stats['health'] -= damage

            # Check if enemy is dead
            if enemy.stats['health'] <= 0:
                return 'You did ' + str(damage) + ' damage and killed the enemy.'
            else:
                outString += 'You did ' + str(damage) + ' damage.\nThe enemy has ' + str(enemy.stats['health']) + ' health left.'

        # Enemy's turn
        # Check player dodge
        playerDodge = player.stats.rollDodge(enemy.stats['agility'])
        if playerDodge:
            outString += 'You dodged.\n'
        # Do damage
        else:
            damage = enemy.stats.rollAttack()
            player.stats['health'] -= damage

            # Check if the player is dead
            if player.stats['health'] <= 0:
                return 'Enemy did ' + str(damage) + ' damage and killed you. Game over.'
            else:
                outString += 'Enemy did ' + str(damage) + ' damage to you.\nYou have ' + str(player.stats['health']) + ' health left.'

        return outString
