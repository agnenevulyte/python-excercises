from sys import argv

script, rezultatai = argv

in_rezultatai = open(rezultatai, 'w')
in_rezultatai.truncate()

print "Hello, I'm %r program." % (script)
print "Please type 3 integer numbers. After each, please press ENTER button."

first_number = int(raw_input("first number: "))
second_number = int(raw_input("second number: "))
third_number = int(raw_input("third number: "))
sum = first_number + second_number + third_number

in_rezultatai = open(rezultatai, 'w')
in_rezultatai.write(str(first_number) + "\n")
in_rezultatai.write(str(second_number) + "\n")
in_rezultatai.write(str(third_number) + "\n")
in_rezultatai.write("sum = %d + %d + %d = %d" % (first_number, second_number, third_number, sum))
in_rezultatai.write("\n")

print "You can find these numbers and their sum in %s.\nCheck it out and find if it's true!" % (rezultatai)

in_rezultatai.close()
