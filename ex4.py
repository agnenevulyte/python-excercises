# assigning a number of cars
cars = 100
# assigning how many people can be  in the car
space_in_a_car = 4.0
# assigning number of drivers
drivers = 30
# assigning number of passangers
passangers = 90
# counting how many cars will be not driven
cars_not_driven = cars - drivers
# counting how many cars will be driven
cars_driven = drivers
# counting how many people can be driven in the cars
carpool_capacity = cars_driven * space_in_a_car
# caclulating the average of passangers per car
average_passengers_per_car = passangers / cars_driven


# print how many available cars we have
print "There are", cars, "cars available."
# print how many drivers we have
print "We have only", drivers, "drivers available."
# print how many cars will be empty
print "There will be", cars_not_driven, "empty cars today."
# print how many people we can transport
print "We can transport", carpool_capacity, "people today."
# print how many passangers we have in total
print "We have", passangers, "to carpool today."
# how many people will sit in each car
print "We need to put about", average_passengers_per_car, "in each car."
