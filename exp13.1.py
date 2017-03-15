from sys import argv

script, first, second, third = argv
name = raw_input("What's your name? ")
age = int(raw_input("How old are you? "))
weight = float(raw_input("How much do you weight in kg? "))
print "The script is called: ", script
print "Hello,", name,". You're", age, "years old and you weight", weight,"kg."
print second + first + third

