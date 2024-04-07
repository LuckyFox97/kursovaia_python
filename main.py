from main_proj.main import base_json, date_check, description_operation, masked_operation

def main():
    # Читаем данные из файла один раз
    operations_data = base_json()

    # Применяем обработку данных
    operations_data = date_check(operations_data)
    operations_data = description_operation(operations_data)

    # Выводим отформатированные данные последних 5 выполненных транзакций
    formatted_transactions = masked_operation(operations_data)
    print(formatted_transactions)

if __name__ == '__main__':
    main()
