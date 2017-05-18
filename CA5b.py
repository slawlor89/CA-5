# Student Number: 10354686
# Student Name: Steven Lawlor
# Submission: CA5(b)


# Create an add function
add = lambda x,y : x+y
print 'Addition function:'
print add(1,1)

# Create a function to convert to fahrenheit
def fahrenheit(temp):
    return ((float(9)/5)*temp + 32)
	
temp = (36.5, 37, 37.5, 39)

F = map(fahrenheit, temp)
print 'Fahrenheit function:'
print F

# Create a function to convert to celsius
def celsius(temp):
    return (float(5)/9*(temp - 32))
	
temp = (36.5, 37, 37.5, 39)

C = map(celsius, F)
print 'Celsius function:'
print C

# Create a fibonacci sequence function
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print 'Fibonacci function:'
print result

# Create a function to find even numbers
def is_even(values):
	return filter(lambda x: x % 2 == 0, values)
	
print 'Is even function:'	
print is_even ([47, 11, 42, 13])

# Create a function to find odd numbers
def is_odd(values):
	return filter(lambda x: x % 2, values)

print 'Is odd function:'	
print is_odd ([47, 11, 42, 13])

# Create a function fo find the max of a set of numbers
def max(values):
	return reduce(lambda a,b: a if (a>b) else b,values)

print 'Max function:'	
print max([47, 11, 42, 13])

# Create a function fo find the min of a set of numbers
def min(values):
	return reduce(lambda a,b: a if (a<b) else b,values)

print 'Min function:'	
print min([47, 11, 42, 13])

# Create a function for divide
def divide(values):
	return reduce(lambda a,b: a/float(b) if (b != 0 and a != 'Nan') else 'Nan',values)

print 'Divide function:'	
print divide([47, 11, 42, 13, 0])

# Create a function for multiply
def multiply(values):
	return reduce(lambda a,b: a*b ,values)

print 'Multiply function:'	
print multiply([47, 11, 42, 13])

# Create a function for a cross product
colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]

print 'Cross product function:'
print coloured_things


# Create a function to create Fibonacci sequence
def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a, b, counter = 0, 1, 0
    while True:
        if (counter >= n): return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)
print 'Fibonacci function:'
for x in f:
    print x,
print


# Create pythagorean triplets
def get_triplets(n):
	for x in range(1,n):
		for y in range(x,n):
			for z in range(y,n):
				if x**2 + y**2 == z**2:
					yield((x,y,z))

triplets = get_triplets(30)
print 'Pythagorean triplets function:'
for triplet in triplets:
	print triplet,
print
