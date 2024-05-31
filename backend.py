import random

date_list = ["sushi date", "paintball date", "stargazing"]

input_date = input("enter date to add to list")

date_list.append(input_date)

for x in date_list:
    print(x)

random_date = random.choice(date_list)

print(str(random_date))
