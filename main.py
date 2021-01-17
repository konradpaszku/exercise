from ex1 import square, factorial, quadratic_function
from ex2 import list_function
from ex3 import Circle
from ex4 import Triangle


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

# test ex 4

triangle_example = Triangle(5, 5)
triangle_example.set_base(10)
triangle_example.set_height(7)
print(triangle_example.get_field_triangle())
print(triangle_example.get_base())
print(triangle_example.get_height())

