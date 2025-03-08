a = 0b10111011
b = 0xC5F
print("Binary is %d, hex is %d" % (a, b))

print("####################")

key = "my_var"
value = 1.234
formatted = "%-10s = %.2f" % (key, value)
print(formatted)

print("####################")

pantry = [
    ("avocados", 1.25),
    ("bananas", 2.5),
    ("cherries", 15),
]
for i, (item, count) in enumerate(pantry):
    print("#%d:%-10s = %.2f" % (i, item, count))

print("####################")


for i, (item, count) in enumerate(pantry):
    print("#%d:%-10s = %d" % (i + 1, item.title(), round(count)))


print("####################")


template = "%s loves food. See %s cook."
name = "Max"
formatted = template % (name, name)
print(formatted)


print("####################")

name = "brad"
formatted = template % (name.title(), name.title())
print(formatted)


print("####################")

key = "my_var"
value = 1.234

old_way = "%-10s = %.2f" % (key, value)
new_way = "%(key)-10s = %(value).2f" % {"key": key, "value": value}
reordered = "%(key)-10s = %(value).2f" % {"value": value, "key": key}
print(old_way)
print(new_way)
print(reordered)

assert old_way == new_way == reordered

print("####################")

name = "Max"
template = "%s loves food. See %s cook."
before = template % (name, name)
template = "%(name)s loves food. See %(name)s cook."
after = template % {"name": name}

print(before)
print(after)

assert before == after


print("####################")


for i, (item, count) in enumerate(pantry):
    before = "#%d:%-10s = %d" % (i + 1, item.title(), round(count))
    print("before__" + before)

    after = "#%(loop)d:%(item)-10s = %(count)d" % {
        "loop": i + 1,
        "item": item.title(),
        "count": round(count),
    }
    print("after__" + after)


print("####################")

c = 1234.5678
formatted = format(c, ",.2f")
print(formatted)

d = "my string"
formatted = format(d, "^20s")
print("*", formatted, "*")


print("####################")

key = "my_var"
value = 1.2345

formatted = "{} = {}".format(key, value)
print(formatted)

formatted = "{:<10} = {:.2f}".format(key, value)
print(formatted)

formatted = "{1} = {0}".format(key, value)
print(formatted)

formatted = "{0} loves food. See {0} cook.".format(name)
print(formatted)


print("####################")

key = "my_var"
value = 1.1234

formatted = f"{key}={value}"
print(formatted)

formatted = f"{key!r:<10}={value:.2f}"
print(formatted)


print("####################")


for i, (item, count) in enumerate(pantry):
    old_style = "#%d:%-10s = %d" % (i + 1, item.title(), round(count))
    print("old_style=", old_style)

    new_style = "#{}:{:<10s}={}".format(i + 1, item.title(), round(count))
    print("new_style=", new_style)

    f_string = f"#{i+1}:{item.title():<10s}={round(count)}"
    print("f_string=", f_string)
