# imports data gets argv feature from sys package.
from sys import argv

script, filename = argv

# open command for txt file
txt = open(filename)
# printing 
print "Here's your file %r:" % filename
# giving a file command of using it. dot is needed
print txt.read()

# open command for txt file
txt = close(filename)
# printing 
print "Here's your file %r:" % filename
# giving a file command of using it. dot is needed
print txt.read()
