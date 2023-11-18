# TODO решите задачу
import json


def multiply() -> float:
    with open('input.json') as f:
        json_data = json.load(f)

    summ = sum(item["score"] * item["weight"] for item in json_data)

    return round(summ, 3)


print(multiply())
