x = ["red", "orange", "yellow", "green", "blue", "purple"]

odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)


print("#" * 20)


x = b"mongoose"
y = x[::-1]
print(y)


print("#" * 20)


x = "寿司"
y = x[::-1]
print(y)

# w = "寿司"
# x = w.encode("utf-8")
# y = x[::-1]
# z = y.decode("utf-8")


print("#" * 20)

x = ["a", "b", "c", "d", "e", "f", "g", "h"]
y = x[::2]
print(y)
z = y[1:-1]
print(z)
