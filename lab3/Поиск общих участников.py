def find_common_participants(participants1, participants2, sep=','):

    participants_list1 = participants1.split(sep)
    participants_list2 = participants2.split(sep)
    participants_common = sorted(list(set(participants_list1).intersection(participants_list2)))

    return participants_common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)
