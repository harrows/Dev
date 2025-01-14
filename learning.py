class Phone:
    line_type = 'Проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзынь!!!!!!!!!!!!')
    
    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')

    def upgrade(self, line_type):
        self.new_dial_type = line_type
        print(f'тип связи {line_type}')

rotary_phone = Phone(dial_type_value='дисковый')

# rotary_phone.ring()

rotary_phone.call('111-222')
rotary_phone.upgrade()

rotary_phone.call('111-222')