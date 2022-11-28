print('Добро пожаловать в расшифровыватель строк!')
a = input('Введите любую строку:')
while len(a)>0:
    bukva = a[0]
    if bukva>='a' and bukva<='z':
        print(bukva, '- маленкая буква')
    elif bukva>='A' and bukva<='Z':
        print(bukva, '- большая буква')
    elif bukva >= 'а' and bukva <= 'я':
        print(bukva, '- маленкая буква')
    elif bukva >= 'А' and bukva <= 'Я':
        print(bukva, '- большая буква')
    elif bukva.isdigit():
        print(bukva, '- цифра')
    else:
        print(bukva, '- знак')
    a = a[1:]