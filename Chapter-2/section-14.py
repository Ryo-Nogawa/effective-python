class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"Tool({self.name}, {self.weight})"


tools = [
    Tool("level", 3.5),
    Tool("hammer", 1.25),
    Tool("screwdriver", 0.5),
    Tool("chisel", 0.25),
]


print("Unsorted:", repr(tools))
tools.sort(key=lambda x: x.name)
print("Sorted:  ", tools)


print("#" * 20)


tools.sort(key=lambda x: x.weight)
print("By weight:", tools)


print("#" * 20)


places = ["home", "work", "New York", "Paris"]
places.sort()
print("Case sensitive:", places)
places.sort(key=lambda x: x.lower())
print("Case insensitive:", places)


print("#" * 20)


power_tools = [
    Tool("drill", 4),
    Tool("circular saw", 5),
    Tool("jackhammer", 40),
    Tool("sander", 4),
]

power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)

power_tools.sort(key=lambda x: (x.weight, x.name), reverse=True)
print(power_tools)

power_tools.sort(key=lambda x: (-x.weight, x.name))
print(power_tools)

power_tools.sort(key=lambda x: x.name)
print("name sort:  ", power_tools)
power_tools.sort(key=lambda x: x.weight, reverse=True)
print("weight sort:", power_tools)
