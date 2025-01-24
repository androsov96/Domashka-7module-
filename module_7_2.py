info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
def custom_write(file_name, strings):
    strings_position = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, line in enumerate(strings):
            start = file.tell()
            file.write(f'{line}\n')
            strings_position[(i + 1 , start )] = line.strip()
    return strings_position

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)