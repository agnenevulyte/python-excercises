def cats_in_the_yard(black_cats, white_cats, colourful_cats):
    print "There are %d black cats in the yard." % black_cats
    print "There are %d white cats in the yard." % white_cats
    print "There are %d colourful cats in the yard." % colourful_cats
    print "So many cats! Can you imagine, how many kittens will be?! \n"

print "Giving function numbers directly:"
cats_in_the_yard(20, 30, 5)

print "Doing variables for the function:"
number_black_cats = 23
number_white_cats = 12
number_colourful_cats = 3
cats_in_the_yard(number_black_cats, number_white_cats, number_colourful_cats)

print "Doing math in the function arguments directly:"
cats_in_the_yard(2 + 4 + 4, 4 + 4 + 7, 7 + 9)

print "Combining math and variables. All at once:"
cats_in_the_yard(number_black_cats + 3, number_white_cats +15, number_colourful_cats +1)

print """I'll ask you to write, how many cats you see in the yard. \n
Each time after you write a number, please press the ENTER button."""
black_cats = int(raw_input("Black cats: "))
white_cats = int(raw_input("White cats: "))
colourful_cats = int(raw_input("Colourful cats: "))

print "So you see %d black cats, %d white cats and %d colourful cats in the yard." % (black_cats, white_cats, colourful_cats)



