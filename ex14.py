from sys import argv

script, year_str = argv
prompt ='# '
year = int(year_str)
print "Now is %d, and I'm the %s script." % (year, script)
print "I'd like to ask you a few questions."
print "Do you think %d would be great from financial perspective? " % year
perspectives = raw_input(prompt)

print "Where did you wish to live by %d? " % year
live = raw_input(prompt)

print "Have you imagined that by the year %d you will have so many electronic devices?\nWhat are your most usable?" % year
electronic = raw_input(prompt)

print """
Alright, so you said %r about financial perspectives.
You wish you live %r. Not sure where that is, but that sounds nice.
And you have %r electronic devices. That's nice.
""" % (perspectives, live, electronic)