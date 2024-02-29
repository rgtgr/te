import csv


def count_errors(reader):
    error_count_dict = {}
    for row in reader:
        title = row[0]
        if title not in error_count_dict:
            error_count_dict[title] = 1
        else:
            error_count_dict[title] += 1
    return error_count_dict


def main():
    count = 0
    with open('game.txt', encoding='utf-8') as f, open('game_new.csv', 'w', encoding='utf-8') as w:
        writer = csv.writer(w, delimiter=' ', lineterminator='\n')
        reader = list(csv.reader(f, delimiter='$'))
        dictt = count_errors(reader)
        for i in reader:
            if count == 0:
                writer.writerow(list(i) + ["counter"])
                count += 1
                continue
            title = i[0]
            writer.writerow(list(map(lambda x: x + ',', i)) + [str(dictt[title])])


if __name__ == '__main__':
    main()
