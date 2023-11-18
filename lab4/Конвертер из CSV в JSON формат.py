import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def csv_to_json() -> None:
    with open(INPUT_FILENAME) as f:
        csv_reader = csv.reader(f)
        headers = next(csv_reader)

        data_list = [dict(zip(headers, row)) for row in csv_reader]

    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(data_list, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    csv_to_json()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
