a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for x in a:
    squares.append(x**2)
print(squares)


print("#" * 20)


squares = [x**2 for x in a]
print(squares)


print("#" * 20)


even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)


print("#" * 20)


even_squares_dict = {x: x**2 for x in a if x % 2 == 0}
threes_cubed_set = {x: x**3 for x in a if x % 3 == 0}
print(even_squares_dict)
print(threes_cubed_set)
