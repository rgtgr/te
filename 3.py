import csv


def main():
    name_of_char = ''
    while not name_of_char:
        name = input("Введите имя персонажа: ")

    with open('game.txt', encoding="utf-8") as f:

        reader = csv.reader(f, delimiter='$')
        list_of_games = []
        names_games = sorted([(value[1], value[0]) for value in reader], key=lambda x: x[0])  # сортируем по именам
        for character_name, game in names_games:
            if name == character_name:
                list_of_games.append(game)

        if len(list_of_games) > 5:
            print(f"Персонаж {name} встречается в играх:")
            for game in list_of_games[:5]:
                print(game)
            print("и др.")
        elif len(list_of_games) == 0:
            print("Этого персонажа не существует")
        else:
            print(f"Персонаж {name} встречается в играх:")
            for game in list_of_games:
                print(game)


if __name__ == '__main__':
    main()
