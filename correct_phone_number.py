import re
# +1 коммит
def is_valid_phone_number(phone_number):
    pattern = '^(\+7|8)\s?(\(?\d{3}\)?\s?\-?)?\d{3}\s?-?\d{2}\s?-?\d{2}$'
    return bool(re.match(pattern, phone_number))

phone1 = "+79991234455"
phone2='9edwu33'
phone3 = "8 999-123-44-55"
print(is_valid_phone_number(phone3))  # Вывод: True


#(\+7|8)- Должно быть +7 или 8 в начале
#\s?- МОЖЕТ стоять(а может и не стоять) пробел
#(\(?)- может стоять скобка под мобильного оператора
#(\d{3})- 3 цифры от 0 до 9 подряд(код оператора)
#(\)?)- может стоять скобка под мобильного оператора
##(\s?)- МОЖЕТ стоять(а может и не стоять) пробел
#(\d{3})- 3 цифры от 0 до 9 подряд
##(\s?)- МОЖЕТ стоять(а может и не стоять) пробел
##(-?)- МОЖЕТ стоять(а может и не стоять) тире
#(\d{3})- 3 цифры от 0 до 9 подряд
##(\s?)- МОЖЕТ стоять(а может и не стоять) пробел
##(-?)- МОЖЕТ стоять(а может и не стоять) тире
#(\d{2})- 2 цифры от 0 до 9 подряд

