import csv

with open('game.txt', encoding='utf-8') as f, open('game_new.txt', 'w', encoding='utf-8') as ff:
    fieldnames = f.readline().strip().split('$')

    reader = csv.DictReader(f, delimiter='$', fieldnames=fieldnames)
    writer = csv.writer(ff, delimiter='$',lineterminator='\n')
    counter = 0
    for k in reader:
        if counter == 0:
            counter+=1
            continue
        title, name, error, date = k["GameName"], k["characters"], k["nameError"], k["date"]
        if '55' in error:
            print(f"У персонажа\t{name}\tв игре\t{title}\tнашлась ошибка с кодом:\t {error}.\tДата фиксации:\t {date}")
            error = "Done"
            date = "0000-00-00"

        writer.writerow([title, name, error, date])
        next(reader)
