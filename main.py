import random

def lottery():
    tickets = [5, 20, 10, 7, 1, 9]
    winner_number = random.choice(tickets)
    return winner_number

winner = lottery()
print(f"The winner number is {winner}!")

def summary(number1, number2):
    result = number1 + number2
    return result

sum = summary(4, 6)
print(sum)

def multi_lottery():
    tickets = [2, 6, 39, 13, 19]
    winner_number1 = random.choice(tickets)
    winner_number2 = random.choice(tickets)
    return winner_number1, winner_number2

winner_1, winner_2 = multi_lottery()

print(f"winner # 1 is {winner_1}, and winner #2 is {winner_2}")
