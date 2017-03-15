people = 40
cars = 15
buses = 10

# asks the question what if.
if cars > people:
    print "We should take the cars."
# asks another question.
elif cars < people:
    print "We should not take the cars."
# if no one answer above is right, else function does its job.
else:
    print "We can't decide."

if buses > cars and buses < people:
    print "That's too many buses."
elif buses < cars and buses < people:
    print "Maybe we could take the buses."
else: 
    print "We still can't decide."


if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay at home then."