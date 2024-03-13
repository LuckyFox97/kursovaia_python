import json

# Открываем файл operations.json и загружаем данные
with open('operations.json', 'r') as file:
    operations_data = json.load(file)


# Выводим информацию о последних операциях
def operation_json():
    for operation in operations_data:
        print("Дата:", operation['date'])
        print("Описание:", operation['description'])
        print("Отправитель:", operation.get('from', 'N/A'))
        print("Получатель:", operation['to'])
        print("Сумма:", operation['operationAmount']['amount'], operation['operationAmount']['currency']['name'])
        print()


operation_json()
