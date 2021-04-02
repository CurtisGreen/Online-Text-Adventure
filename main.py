from flask import Flask, request, render_template, session

app = Flask(__name__)
app.secret_key = b';l235]-9i0;nkawef9u[0]'

@app.route('/', methods=['POST', 'GET'])
def home():
    text = None
    # Get text from html form
    if 'text' in request.form:
        text = request.form['text']
    return processCommand(text)

# Actual logic would go here
# Currently just capitalizes text and adds it to the stack
def processCommand(command):
    if (command != None):
        result = command.upper()
        addCommand(result)

    commands = getCommands()
    return displayPage(commands)

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

def displayPage(commands = []):
    return render_template('main.html', commands = commands)