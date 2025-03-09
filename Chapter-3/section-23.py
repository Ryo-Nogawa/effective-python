def remainder(number, divisor):
    return number % divisor


assert remainder(20, 7) == 6


my_kwargs = {"divisor": 7}
assert remainder(number=20, **my_kwargs) == 6

my_kwargs = {"number": 20}
other_kwargs = {"divisor": 7}
assert remainder(**my_kwargs, **other_kwargs) == 6


def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


print_parameters(alpha=1.5, beta=9, gamma=4)


print("#" * 20)


def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period


weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print(f"{flow:.3} kg per second")

flow_per_second = flow_rate(weight_diff, time_diff)
print(f"flow_per_second={flow_per_second}")
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)
print(f"flow_per_hour={flow_per_hour}")
