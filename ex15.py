# imports data gets argv feature from sys package.
from sys import argv

script, filename = argv

# open command for txt file
txt = open(filename)
# printing 
print "Here's your file %r:" % filename
# giving a file command of using it. dot is needed
print txt.read()

# printing
print "Type the filename again:"
# letting type to custumer file name
file_again = raw_input("> ")

# open command for txt file
txt_again = open(file_again)

# giving a file command of using it. dot is needed
print txt_again.read()