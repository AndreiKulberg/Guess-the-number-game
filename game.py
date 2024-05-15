import random

def generate_number():
    return random.randint(1, 10)

def check_guess(secret_number, guess):
    if guess > secret_number:
        return "Меньше"
    elif guess < secret_number:
        return "Больше"
    else:
        return "Ура! Вы угадали!"

def main():
    while True:
        secret_number = generate_number()
        attempts = 0

        print("Давайте играть в угадай число! Я загадал число от 1 до 10.")
        
        while True:
            try:
                guess = int(input("Попробуйте угадать: "))
                attempts += 1

                result = check_guess(secret_number, guess)
                print(result)

                if result == "Ура! Вы угадали!":
                    print(f"Потребовалось {attempts} попыток.")
                    break
            except ValueError:
                print("Пожалуйста, введите целое число.")
        
        play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
        if play_again != "да":
            print("Спасибо за игру! До свидания!")
            break

main()