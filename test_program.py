<<<<<<< HEAD
# class Phone:

#     line_type = 'проводной'

#     def __init__(self, dial_type_value):
#         self.dial_type = dial_type_value

#     def ring(self):
#         print('Дзззззыыыыыыыынь!')

#     def call(self, phone_number):
#         print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')

#     # Ещё один метод.
#     def get_missed_calls(self):
#         print('Запрос количества пропущенных вызовов.')


# rotary_phone = Phone(dial_type_value='дисковый')


# print(rotary_phone.dial_type)

# rotary_phone.dial_type = 'кнопочный'

# print(rotary_phone.dial_type)
# rotary_phone.get_missed_calls()

# Skill percentages for various programming languages
bash = 31
c_and_c_plus_plus = 29
c_sharp = 11
html_css = 36
java = 19
javascript = 37
sql = 34


def analyze_skills():
    minimum = min(bash, c_and_c_plus_plus, c_sharp, html_css, java, javascript, sql)
    maximum = max(bash, c_and_c_plus_plus, c_sharp, html_css, java, javascript, sql)

    print(
        "Доля питонистов, "
        "у которых есть наименее "
        "популярный навык (в %):",
        minimum
    )
    print(
        "Доля питонистов, "
        "у которых есть наиболее "
        "популярный навык (в %):",
        maximum
    )

analyze_skills()

=======
try:
    import practicum
except ImportError:
    raise AssertionError('Модуль `practicum` не обнаружен.')

EXPECTED_FUNC_NAME = 'say_hello'

def test_say_hello_exists():
    assert hasattr(practicum, EXPECTED_FUNC_NAME), (
        f'Функция `{EXPECTED_FUNC_NAME}` не обнаружена в модуле `practicum`')

def test_say_hello_run_without_exceptions():
    try:
        practicum.say_hello()
    except Exception as error:
        raise AssertionError(
            f'При запуске функции `{EXPECTED_FUNC_NAME}` возникло '
            f'исключение: {type(error).__name__}: {error}`'
        ) 
>>>>>>> 9ef3fd71899f93b93d0f11b3210becdd328f7795
