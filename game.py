import random

def generate_number(min_value, max_value):
    return random.randint(min_value, max_value)

def check_guess(secret_number, guess):
    if guess > secret_number:
        return "Меньше"
    elif guess < secret_number:
        return "Больше"
    else:
        return "Ура! Вы угадали!"

def main():
    best_score = None
    while True:
        print("Выберите уровень сложности:")
        print("1. Легкий (числа от 1 до 50, 5 попыток)")
        print("2. Средний (числа от 1 до 100, 10 попыток)")
        print("3. Сложный (числа от 1 до 200, 15 попыток)")
        
        difficulty = input("Введите номер уровня сложности: ").strip()
        if difficulty == '1':
            min_value, max_value, max_attempts = 1, 50, 5
        elif difficulty == '2':
            min_value, max_value, max_attempts = 1, 100, 10
        elif difficulty == '3':
            min_value, max_value, max_attempts = 1, 200, 15
        else:
            print("Некорректный выбор. Попробуйте снова.")
            continue

        secret_number = generate_number(min_value, max_value)
        attempts = 0
        history = []

        print(f"Давайте играть в угадай число! Я загадал число от {min_value} до {max_value}.")
        print(f"У вас есть {max_attempts} попыток угадать число.")
        
        while attempts < max_attempts:
            try:
                guess = input("Попробуйте угадать (или введите 'выход' для завершения игры): ")
                if guess.strip().lower() == 'выход':
                    print("Спасибо за игру! До свидания!")
                    return
                
                guess = int(guess)
                attempts += 1
                history.append(guess)

                result = check_guess(secret_number, guess)
                print(result)

                if result == "Ура! Вы угадали!":
                    print(f"Потребовалось {attempts} попыток.")
                    if best_score is None or attempts < best_score:
                        best_score = attempts
                        print("Поздравляем! Это новый рекорд!")
                    break
            except ValueError:
                print("Пожалуйста, введите целое число.")
        
        if attempts == max_attempts:
            print(f"Вы исчерпали {max_attempts} попыток. Загаданное число было {secret_number}.")

        print("История ваших попыток: ", history)

        play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
        if play_again != "да":
            print("Спасибо за игру! До свидания!")
            break

main()
