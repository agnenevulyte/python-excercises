print "What's your name?",
name = raw_input()
print "What's your surname?",
surname = raw_input()
print "Please type the year you were born:",
birth_year = int(raw_input())
print "Please write your gender (male/female):",
gender = raw_input()
print "Please type your height in m:",
height = float(raw_input())
print "Please type your weight in kg:",
weight = int(raw_input())

KMI = weight/(height * height)
print "Dear %s %s (%d) your KMI index is %5.2f" % (name, surname, birth_year, KMI)
