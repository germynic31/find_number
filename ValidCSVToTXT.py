import csv
import phonenumbers as pn


def validate_phone_numbers(csv_file, output_file):
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            with open(output_file, 'w') as output:
                for row in reader:
                    phone_number = '+' + row[1]  # Добавляем знак "+" перед номером
                    try:
                        parsed_number = pn.parse(phone_number, None)
                        if pn.is_valid_number(parsed_number):
                            name = row[0]
                            operator = row[2]
                            output.write(f"Номер: {phone_number}, ")
                            output.write(f"Имя: {name}, ")
                            output.write(f"Оператор: {operator}\n")
                    except pn.phonenumberutil.NumberParseException:
                        pass
        print("Результаты проверки записаны в файл valid.txt.")
    except FileNotFoundError:
        print('Файл формата csv не найден, проверьте "csv_file_path"')


csv_file_path = 'input.csv'
output_file_path = 'valid.txt'

validate_phone_numbers(csv_file_path, output_file_path)
