a = ["a", "b", "c", "d", "e", "f", "g", "h"]
print("Middle two: ", a[3:5])
print("All but ends: ", a[1:7])


print("#" * 20)


b = a[3:]
print("Before: ", b)
b[1] = 99
print("After: ", b)
print("No change: ", a)


print("#" * 20)


print("Before: ", a)
a[2:7] = [99, 22, 14]
print("After: ", a)

b = a[:]
assert b == a and b is not a

b = a
print("Before a", a)
print("Before b", b)
a[:] = [101, 102, 103]
assert a is b
print("After a", a)
print("After b", b)
