# def starts the function. we are giving function the name and writing arguments inside ().
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

# we are giving arguments in numbers straight to our function.
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# we are making variables to each of our arguments with changed names.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# ..and then printing arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# We are doing math instead of arguments in words.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# We are doing math and variables sum in arguments field.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)