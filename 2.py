import csv


def main():
    name = input("Введите имя персонажа: ")

    with open('game.txt', encoding="utf-8") as f:
        print(f.readline())
        reader = csv.reader(f, delimiter='$')
        list_of_games = []
        names_games = sorted([(value[1], value[0]) for value in reader], key=lambda x: x[0]) #сортируем п оименам
        for character_name, game in names_games:
            if name == character_name:
                list_of_games.append(game)
        print(f"Персонаж {name} встречается в играх:")
        if len(list_of_games) > 5:
            for game in list_of_games[:5]:
                print(game)
            print("и др.")
        else:
            for game in list_of_games:
                print(game)


if __name__ == '__main__':
    main()
