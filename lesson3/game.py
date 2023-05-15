import numpy as np

random_number = np.random.randint(1, 201)

count = 0

while True:
    count+= 1
    predict_number = int(input("Gues a secret number from 1 to 200: "))
    if predict_number > random_number:
        print(f"{predict_number} is higher than secret number")
    elif predict_number < random_number:
        print(f"{predict_number} is lower than secret number")
    else:
        print(f"Yes secret number is {predict_number}, you won after {count} tries")
        break
