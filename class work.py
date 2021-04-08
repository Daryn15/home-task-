class Person:
    #     # конструктор
    #
    def __init__(self, name, salary):
        self.name = name  # устанавливаем имя
        self.salary = salary

    def display_info(self):
        print("Привет, меня зовут", self.name, "и моя зп", self.salary)

    # #объект   #класс


person1 = Person("Daryn", 1000)  # объект наш 1

# #объект  #функция
person1.display_info()  # Привет, меня зовут Daryn и моя зп 1000



