def analyze_object(obj):
    print(f"Тип объекта: {type(obj)}")
    print(f"Атрибуты и методы: {dir(obj)}")
    
    if hasattr(obj, '__dict__'):
        print(f"Атрибуты экземпляра: {obj.__dict__}")
    else:
        print("У объекта нет `__dict__`")

    print(f"Имя класса: {obj.__class__.__name__}")

analyze_object(42)