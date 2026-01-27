import logging

logging.basicConfig(level=logging.INFO)

def parse_file(filename):
    data = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    key, value = line.split("=")

                    # пробуем преобразовать в число
                    if value.isdigit():
                        value = int(value)

                    data[key] = value

                except ValueError:
                    logging.warning(f"Неверный формат строки: {line}")

    except FileNotFoundError:
        logging.error("Файл не найден")

    return data


result = parse_file("text.txt")
print(result)



