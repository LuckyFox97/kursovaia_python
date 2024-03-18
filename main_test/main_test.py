import json

def main():
    # Чтение данных из файла operations.json
    with open('main/operations.json', 'r') as file:
        data = json.load(file)

    # Обработка данных и вывод информации о транзакциях
    for transaction in data:
        print("Transaction ID:", transaction['id'])
        print("Date:", transaction['date'])
        print("Amount:", transaction['operationAmount']['amount'], transaction['operationAmount']['currency']['code'])
        print("Description:", transaction['description'])
        if 'from' in transaction:
            print("From:", transaction['from'])
        if 'to' in transaction:
            print("To:", transaction['to'])
        print()

if __name__ == '__main__':
    main()
