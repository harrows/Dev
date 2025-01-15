class BacteriaProducer:
    # Допишите инициализатор класса:
    # Задайте два атрибута экземпляра:
    # Первый хранит максимальное количество бактерий
    # Второй хранит текущее количество бактерий (по умолчанию 0)
    def __init__(self, max_bacteria):
        self.max_bacteria = max_bacteria
        self.current_bacteria_count = 0

    # Допишите метод, добавляющий бактерию в чашу
    # Если уже достигнуто максимальное число бактерий,
    # то добавлять новую нельзя, выведите сообщение об ошибке
    def create(self):
        if self.current_bacteria_count < self.max_bacteria:
            self.current_bacteria_count += 1
            print(f'Добавлена одна бактерия. Бактерий в колонии: {self.current_bacteria_count}')
        else:
            print(f'Нет места под новую бактерию')

    # Допишите метод, удаляющий бактерию из чаши.
    # Если в чаше уже нет бактерий, то удалять нечего;
    # выведите сообщение об ошибке
    def delete(self):
        if self.current_bacteria_count > 0:
            self.current_bacteria_count -= 1
            print(f'Одна бактерия удалена. Бактерий в колонии: {self.current_bacteria_count}')
        else:
            print(f'В популяции нет бактерий, удалять нечего')


# Пример запуска для самопроверки
bacteria_producer = BacteriaProducer(max_bacteria=3)
bacteria_producer.delete()
bacteria_producer.create()
bacteria_producer.create()
bacteria_producer.create()
bacteria_producer.create()
bacteria_producer.delete()