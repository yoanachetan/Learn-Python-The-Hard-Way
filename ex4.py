# Sets variable "cars" to "100"
cars = 100

# Sets variable "space_in_the_car" to "4.0"
space_in_a_car = 4.0 

# Sets variable "drivers" to "30"
drivers = 30 

# Sets variable "passengers" to "90"
passengers = 90 

# Sets variable "cars_not_driven" to the variable "cars" minus the variable "drivers" = 100 - 30
cars_not_driven = cars - drivers

# Sets variable "cars_driven" to variable "drivers" = 30
cars_driven = drivers 

# Sets variable "carpool_capacity" to variable "drivers"multiplied by variable "space_in_a_car" = 30 * 4.0
carpool_capacity = cars_driven * space_in_a_car  

# Sets the variable "average_passengers_per_car" to variable "passengers" divided by "cars_driven"
average_passengers_per_car = passengers / cars_driven  


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
