import numpy as np

number = np.random.randint(1, 101)
count = 0

while True:
    count += 1
    predict_number = int(input("Guess a number from 1 to 100"))

    if predict_number > number:
        print("Number is smaller")
    elif predict_number < number:
        print("Number is greater")
    else:
        print(f"You guessed right on {count} try, the number is {number}!")
        break
