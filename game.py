import random

def generate_number():
    return random.randint(1, 100)

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
        secret_number = generate_number()
        attempts = 0
        max_attempts = 10

        print("Давайте играть в угадай число! Я загадал число от 1 до 100.")
        print(f"У вас есть {max_attempts} попыток угадать число.")
        
        while attempts < max_attempts:
            try:
                guess = input("Попробуйте угадать (или введите 'выход' для завершения игры): ")
                if guess.strip().lower() == 'выход':
                    print("Спасибо за игру! До свидания!")
                    return
                
                guess = int(guess)
                attempts += 1

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

        play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
        if play_again != "да":
            print("Спасибо за игру! До свидания!")
            break

main()
