import numpy as np

def random_predict(number: int=1) -> int:
    count = 0
    
    while True:
        count+= 1
        predict_num = np.random.randint(1, 101)
        if number == predict_num:
            break
        
    return count

def score_game(random_predict) -> int:
    count_list = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    
    for number in random_array:
        count_list.append(number)
        
    score = int(np.mean(count_list)) # mean находит среднее число
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

if __name__ == "__main__":
    score_game(random_predict)
