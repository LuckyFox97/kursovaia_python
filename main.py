from main_proj.main import OperationsProcessor

# Создаем экземпляр класса и обрабатываем данные
processor = OperationsProcessor()
processor.date_check()
processor.description_operation()

# Выводим отформатированные данные последних 5 выполненных транзакций
formatted_transactions = processor.masked_operation()
print(formatted_transactions)
