# Handles the saving and reading of the player progress

def save(filename, level):
    f = open(filename, 'w')
    f.write(level)
    f.close()

def read(filename):
    f = open(filename, 'r')
    return f.read()