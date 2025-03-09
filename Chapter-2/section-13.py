cars_ages = [0, 9, 4, 8, 7, 20, 1, 6, 15]
car_ages_descending = sorted(cars_ages, reverse=True)
print("result_descending: ", car_ages_descending)

oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest, second_oldest, others)


print("#" * 20)


oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)

oldest, *others, youngest = car_ages_descending
print(oldest, youngest, others)

*others, second_youngest, youngest = car_ages_descending
print(youngest, second_youngest, others)
