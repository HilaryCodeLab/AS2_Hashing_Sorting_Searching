import csv
from chess_player import Chessplayer


def read_csv(file):
    """

    :param file: csv
    :return: object list
    """
    data = []
    # open csv file and read each lines, lines are seperated with comma
    with open(file, encoding="utf-8", mode='r')as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1 
            else:
                line_count +=1
                lname = row[0].strip()
                fname = row[1].strip()
                full_name = row[2].strip()
                country = row[3].strip()
                born = row[4].strip()
                died = row[5].strip()
                player = Chessplayer(lname,fname,full_name,country,born,died)
                data.append(player)
        return data

    





