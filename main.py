from ex1 import square, factorial, quadratic_function
from ex2 import list_function
from ex3 import Circle


#test ex 1

print(square(3))
print(factorial(14))
print(quadratic_function(5, 3, 6))


# test ex 2

print(list_function([1, 4, 6, 7, 20]))

# test ex 3

circle_example = Circle(1)
circle_example.set_radius(5)
print(circle_example.get_circuit())
print(circle_example.get_field())
print(circle_example.get_radius())




