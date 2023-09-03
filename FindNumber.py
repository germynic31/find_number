import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type
import time
from phone_func import type_phone

phone = input('Введите номер для поиска данных (Ввод номера через код страны +7, +375, +380): ')
try:
    parsed_phone = phonenumbers.parse(phone)
    valid = phonenumbers.is_valid_number(parsed_phone)

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
    else:
        print('''Номер невалидный!!!
   
Попробуйте перезапустить программу и ввести номер в таком шаблоне
       ↓↓↓
+1 234 567 89 10''')
except:
    print('''Номер введен без кода страны или его не существует!!!''')
