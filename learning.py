class Person():
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def greet(self):
        return f'Привет, меня зовут {self.name}, мне {self.age} лет, я из города {self.city}.'
    
man = Person('Василий', 23, 'Москва')
print(man.greet())
