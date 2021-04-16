class Parser():
    def parse(self, input):
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
        actions = {'move', 'go'}
        return (action in actions)
    
    def verifyDirection(self, dir):
        directions = {'up', 'down', 'left', 'right', 'north', 'south', 'east', 'west', 'forwards', 'backwards'}
        return (dir in directions)


    def checkAttack(self, inputArr):
        actions = {'attack', 'hit', 'kill'}
        # 1 word action ('attack'), attack current target if it exists
        if len(inputArr) == 1 and inputArr[0] in actions:
            return 'There is nothing to attack here'
        # 2 word action ('attack goblin'), attack if that target exists
        elif len(inputArr) == 2 and inputArr[0] in actions:
            return 'There is no ' + inputArr[1] + ' to attack here'
        else:
            return None