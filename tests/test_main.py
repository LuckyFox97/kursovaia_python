from main_proj.main import mask_card, date_check, base_json


class TestMainProj:
    def test_mark_account_number(self):
        """Корректно маскируется номер счета"""
        assert mask_card('Счет 35383033474447895560') == 'Счет 5560'

    def test_mark_card_number(self):
        """Корректно маскируется номер карты"""
        assert mask_card('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
        assert mask_card('Visa Classic 1596837868705199') == 'Visa Classic 1596 83** **** 5199'

    def test_date_check(self):
        """Корректно форматирует время"""
        data = [
            {'date': '2018-04-16T17:34:19.241289'},
            {'date': '2022-12-25T08:15:30.123456'}
        ]

        expected_output = [
            {'date': '16.04.2018'},
            {'date': '25.12.2022'}
        ]

        assert date_check(data) == expected_output

    def test_base_json(self):
        """Корректно выводит из базы данные"""
        assert base_json == {"key": "value"}
