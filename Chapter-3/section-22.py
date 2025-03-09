def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{message}: {values_str}")


log("My numbers are", [1, 2])
log("Hi there", [])


print("#" * 20)


def log2(message, *values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{message}: {values_str}")


log2("My numbers are", 1, 2)
log2("Hi there")


print("#" * 20)


def log3(sequence, message, *values):
    if not values:
        print(f"{sequence} - {message}")
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{sequence} - {message}: {values_str}")


log3(1, "Favorites", 7, 33)
log3(1, "Hi there")
log3("Favorite numbers", 3, 33)
