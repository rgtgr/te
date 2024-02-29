import csv


def main():
    """
    Открывает файл, котоырй нужно исправить, исправляет его, и добавляет исправленные значения в файл game_new.txt

    """
    with open('game.txt', encoding='utf-8') as f, open('game_new.csv', 'w', encoding='utf-8') as ff:
        reader = csv.reader(f, delimiter='$')
        writer = csv.writer(ff, delimiter=' ', lineterminator='\n')
        counter = 0
        for k in reader:  # Игнорируем строку с названием столбцов
            if counter == 0:
                counter += 1
                continue
            title, name, error, date = k[0], k[1], k[2], k[3]
            if '55' in error:
                print(
                    f"У персонажа\t{name}\tв игре\t{title}\tнашлась ошибка с кодом:\t {error}.\tДата фиксации:\t {date}")
                error = "Done"
                date = "0000-00-00"

            writer.writerow(list(map(lambda x: x + ',', [title, name, error])) + [date])
                                                           # добавляем в новый файл исправленную строку. Добавляем пробел
            next(reader)


if __name__ == '__main__':
    main()
