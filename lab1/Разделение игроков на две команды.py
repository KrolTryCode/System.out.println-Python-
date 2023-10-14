list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
# TODO Разделите участников на две команды
print(list_players[0:int(len(list_players)/2):1], "\n", list_players[int(len(list_players)/2):len(list_players):1], sep = "")

