from flask import Flask, request, render_template, session
from Parser import Parser

app = Flask(__name__)
app.secret_key = b';l235]-9i0;nkawef9u[0]'

@app.route('/command', methods=['POST'])
def home():
    text = None
    print('home()')
    # Get text from html form
    jsonData = request.get_json()
    if 'command' in jsonData:
        text = jsonData['command']
    print(text)
    return processCommand(text)

# Actual logic would go here
# Currently just capitalizes text and adds it to the stack
def processCommand(command):
    if (command != None):
        parser = Parser()
        result = parser.parse(command)
        addCommand(result)

    commands = getCommands()
    return {'commands': commands}

# Get command list out of session storage
def getCommands():
    commands = session.get('commands')
    if (commands == None):
        return []
    else:
        return commands

# Store command in a list in session storage
def addCommand(command):
    maxCommands = 5
    commands = getCommands()

    # Remove first command
    if len(commands) >= maxCommands:
        commands.pop(0)
    
    commands.append(command)
    session['commands'] = commands