import random

def play_game():
    print("Гра 'Камінь, ножиці, папір'")

    choices = ["камінь", "ножиці", "папір"]

    while True:
        computer_choice = random.choice(choices)

        player_choice = input("Виберіть камінь, ножиці або папір (або 'вийти', щоб закінчити гру): ").lower()

        if player_choice == "вийти":
            break

        if player_choice not in choices:
            print("Неправильний вибір. Спробуйте ще раз.")
            continue

        print("Ваш вибір:", player_choice)
        print("Вибір комп'ютера:", computer_choice)

        if player_choice == computer_choice:
            print("Нічия!")
        elif (player_choice == "камінь" and computer_choice == "ножиці") or \
                (player_choice == "ножиці" and computer_choice == "папір") or \
                (player_choice == "папір" and computer_choice == "камінь"):
            print("Ви перемогли!")
        else:
            print("Комп'ютер переміг!")

        print()

    print("Дякую за гру!")
play_game()