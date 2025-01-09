class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')

    # Ещё один метод.
    def get_missed_calls(self):
        print('Запрос количества пропущенных вызовов.')

rotary_phone = Phone(dial_type_value='дисковый')
print(rotary_phone.dial_type)

rotary_phone.dial_type = 'кнопочный'

print(rotary_phone.dial_type)
rotary_phone.get_missed_calls()