from datetime import datetime
import json
import os

class OperationsProcessor:
    def __init__(self):
        self.operations_data = self.base_json()

    def base_json(self):
        file_path = os.path.join(os.path.dirname(__file__), 'operations.json')  # Исправлено на __file__
        with open(file_path) as json_file:
            data = json.load(json_file)
        return data

    def date_check(self):
        for operation in self.operations_data:
            if 'date' in operation:
                date_str = operation['date']
                operation_date = datetime.fromisoformat(date_str)
                formatted_date = operation_date.strftime('%d.%m.%Y')
                operation['date'] = formatted_date

    def description_operation(self):
        for operation in self.operations_data:
            if 'description' in operation:
                description = operation['description']
                description = description.replace("/", "")
                operation['description'] = description

    def mask_card(self, card):
        if "Счет" in card:
            masked_card = f"Счет {card[-4:]}"
        else:
            card_type = card.split(' ')
            card_number = card[-16:]
            if len(card_type) == 2:
                masked_card = f"{card_type[0]} {card_number[:4]} {card_number[4:6]} **** {card_number[-4:]}"
            else:
                masked_card = f"{card_type[0]} {card_type[1]} {card_number[:4]} {card_number[4:6]} **** {card_number[-4:]}"
        return masked_card

    def masked_operation(self):
        sorted_data = [operation for operation in self.operations_data if 'date' in operation and operation.get('state') == 'EXECUTED']
        sorted_data = sorted(sorted_data, key=lambda x: datetime.strptime(x['date'], '%d.%m.%Y'), reverse=False)[-7:]

        result = ""
        for operation in sorted_data:
            if 'from' in operation and 'to' in operation and 'operationAmount' in operation:
                from_ = operation.get('from', 'Unknown')
                to_ = operation.get('to', 'Unknown')
                amount = operation['operationAmount']['amount']
                currency = operation['operationAmount']['currency']['name']

                if "Счет" in from_:
                    masked_from = f"Счет {from_[-4:]}"
                else:
                    masked_from = self.mask_card(from_)

                if "Счет" in to_:
                    masked_to = f"Счет {to_[-4:]}"
                else:
                    masked_to = self.mask_card(to_)

                result += f"{operation['date']} {operation['description']}\n{masked_from} -> {masked_to}\n{amount} {currency}\n\n"

        return result

