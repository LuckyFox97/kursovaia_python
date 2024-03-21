from main_proj.main import base_json, date_check, discription_operation
import json
import os
from datetime import datetime

def test_base_json():
    file_path = os.path.join(os.path.dirname(__file__), 'operations.json')
    with open(file_path) as json_file:
        data = json.load(json_file)
    assert isinstance(data, list)


def test_discription_operation():
    data = base_json()
    for operation in data:
        if 'description' in operation:
            description = operation['description']
            description = description.replace("/", "")
            assert operation['description'] == description

def test_masked_operation():
    data1 = date_check()
    data = discription_operation()

    sorted_data = [operation for operation in data1 if 'date' in operation and operation.get('state') == 'EXECUTED']
    sorted_data = sorted(sorted_data, key=lambda x: datetime.strptime(x['date'], '%d.%m.%Y'), reverse=False)[-7:]

    result = ""
    for operation in sorted_data:
        if 'from' in operation and 'to' in operation and 'operationAmount' in operation:
            from_ = operation.get('from', 'Unknown')
            to_ = operation.get('to', 'Unknown')
            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['name']

            if "Счет" in from_:
                masked_from = f"Счет **{from_[-4:]}"
            else:
                card_type = from_.split(' ')
                if len(card_type) == 2:
                    card_number = from_[-16:]
                    masked_from = f"{card_type[0]} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
                else:
                    card_number = from_[-16:]
                    masked_from = f"{card_type[0]} {card_type[1]} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


            if "Счет" in to_:
                masked_to = f"Счет **{to_[-4:]}"
            else:
                card_type = to_.split(' ')
                if len(card_type) == 2:
                    card_number = to_[-16:]
                    masked_to = f"{card_type[0]} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
                else:
                    card_number = to_[-16:]
                    masked_to = f"{card_type[0]} {card_type[1]} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

            result += f"{operation['date']} {operation['description']}\n{masked_from} -> {masked_to}\n{amount} {currency}\n\n"

    formatted_transactions = result
    assert formatted_transactions == formatted_transactions
