from sys import argv

script, filename = argv

txt = open(filename, 'r')

print "We're going to read what's written in %r" % filename
print txt.read()