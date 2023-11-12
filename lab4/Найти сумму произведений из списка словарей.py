# TODO решите задачу
import json


def multiply() -> float:
    with open('input.json') as f:
        json_data = json.load(f)

    summ = 0
    for item in json_data:
        summ += item["score"] * item["weight"]

    return round(summ, 3)


print(multiply())
