# Student Number 10354686
# Student Name: Steven Lawlor
# Continuous Assignment 5

# The following R script is used to create a set of 10 functions as part of a 
# calculator. The calculator will allow the user the ability to perform the following
# functions;
# XXXXXX

# Create the addition function
addition <- function(x,y) {
  return(x+y)
}

# Create the subtraction function
subtraction <- function(x,y) {
  return(x-y)
}

# Create the multiplication function
multiplication <- function(x,y) {
  return(x*y)
}

# Create the division function
division <- function(x,y) {
  return(x/y)
}

# Create the exponent function
exponential <- function(x,y) {
  return(x^y)
}

# Create the square root function
sqroot <- function(x) {
  return(sqrt(x))
}

# Create the Cos function
cosfunction <- function(x) {
  return(cos(x*pi/180))
}

# Create the Cos function
sinfunction <- function(x) {
  return(sin(x*pi/180))
}

# Create the Tan function
# We must ensure that we can gracefull handle both 180 degrees and 90 degrees
logfunction <- function(x) {
  return(log(x))
}

# Create the factorial function
factorialfunction <- function(x) {
  return(factorial(x))
}



# The following are tests to confirm that the calculator works as expected
print("The following are confirmations that the functions work correctly...")
# Test the addition function
print("Test to confirm that 3 + 4 equals 7")
print(addition(3,4))

# Test the subtraction function
print("Test to confirm that 3 - 4 equals -1")
print(subtraction(3,4))

# Test the multiplication function
print("Test to confirm that 3 * 4 equals 12")
print(multiplication(3,4))

# Test the division function
print("Test to confirm that 3 / 4 equals 0.75")
print(division(3,4))

# Test the exponent function
print("Test to confirm that 3 ^ 4 equals 81")
print(exponential(3,4))

# Test the square root function
print("Test to confirm that square root 16 equals 4")
print(sqroot(16))

# Test the cos function
print("Test to confirm that cos(0) equals 1")
print(cosfunction(0))

# Test the sin function
print("Test to confirm that sin(90) equals 1")
print(sinfunction(90))

# Test the log function
print("Test to confirm that log 10 equals 2.302585")
print(logfunction(10))

# Test the factorial function
print("Test to confirm that 4 factorial equals 24")
print(factorialfunction(4))
