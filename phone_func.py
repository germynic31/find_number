from phonenumbers import number_type
import csv


def type_phone(number):
    if number_type(number) == 0:
        print('Это стационарный телефон')
        return ''
    elif number_type(number) == 1:
        print('Это мобильный телефон')
        return ''
    elif number_type(number) == 2:
        print('Этот номер телефона может быть как стационарным, так и мобильным')
        return ''
    elif number_type(number) == 3:
        print('Это бесплатный номер. Этот тип номера телефона предоставляется без оплаты для вызывающего')
        return ''
    elif number_type(number) == 4:
        print('Этот номер телефона связан с услугами, которые взимают дополнительную плату за вызов')
        return ''
    elif number_type(number) == 5:
        print('Этот номер телефона предоставляет разделение стоимости звонка между вызывающим и владельцем номера')
        return ''
    elif number_type(number) == 6:
        print('Этот номер телефона связан с услугами голосовой связи через интернет (VoIP)')
        return ''
    elif number_type(number) == 7:
        print('Этот номер телефона предоставляется для персонального использования')
        return ''
    elif number_type(number) == 8:
        print('Этот номер телефона связан с пейджером')
        return ''
    elif number_type(number) == 9:
        print('Этот номер телефона предоставляется для специальных услуг доступа (UAN)')
        return ''
    elif number_type(number) == 10:
        print('Этот номер телефона связан с голосовой почтой')
        return ''
    else:
        print("Этот номер телефона не может быть определен")
        return ''


def check_number_in_csv(number, csv_file):
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if number in row:
                return True
    return False
