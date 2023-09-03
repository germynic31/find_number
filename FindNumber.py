import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type
import time
from phone_func import type_phone, check_number_in_csv

phone = input('Введите номер для поиска данных (Ввод номера через код страны +7, +375, +380): ')
try:
    parsed_phone = phonenumbers.parse(phone)
    valid = phonenumbers.is_valid_number(parsed_phone)
    number_to_check = phone[1:]
    csv_file_path = 'input.csv'

    if valid:
        print('Номер валидный, производится поиск данных...')
        time.sleep(1)
        print(type_phone(parsed_phone))
        time.sleep(3)
        print(
            "Национальный номер: " + phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.NATIONAL))
        time.sleep(0.5)
        print("Регистрация номера: " + geocoder.country_name_for_number(parsed_phone, 'ru'),
              geocoder.description_for_number(parsed_phone, 'ru'), sep=', ')
        time.sleep(0.5)
        print("Временная зона:", ' '.join(timezone.time_zones_for_geographical_number(parsed_phone)))
        time.sleep(0.5)
        if number_type(parsed_phone) != 0:
            print("Мобильный оператор: " + carrier.name_for_number(parsed_phone, lang='ru'))
        else:
            print("Мобильного оператора нет")
        time.sleep(0.5)
        if check_number_in_csv(number_to_check, csv_file_path):
            print("Номер найден в файле CSV.")
        else:
            print("Номер не найден в файле CSV.")
    else:
        print('''Номер невалидный!!!
   
Попробуйте перезапустить программу и ввести номер в таком шаблоне
       ↓↓↓
+1 234 567 89 10''')
except FileNotFoundError:
    print('Файл формата csv не найден, проверьте "csv_file_path"')
except:
    print("Вы неправильно ввели номер или же такой код страны не существует")
