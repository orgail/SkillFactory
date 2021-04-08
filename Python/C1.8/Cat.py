class Cat:
    def __init__(self, name, gender, age):
        self.name = str(name)
        self.gender = str(gender)
        self.age = str(age)

    def print_cats(self):
        return f'Имя: {self.name}\nПол: {self.gender}\nВозраст: {self.age}'