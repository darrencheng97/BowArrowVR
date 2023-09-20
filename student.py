from person import Person

class Student(Person):
    # Inherited from Person. inherit后会复制一份person的objects复制到Student的最上面
    # def __init__(self, name, age) :
    #     self.name = name
    #     self.age = age
    
    # def print_name(self):
    #     print(self.name)
    
    # def print_age(self):
    #     print(self.age)

    # 程式码有了遗传后可以把它精简成以下这样
    def __init__(self, name, age, school) :
        self.name = name
        self.age = age
        self.school = school
    
    # Can remove these two function since the print name and print age are inherited from Person
    # def print_name(self):
    #     print(self.name)
    
    # def print_age(self):
    #     print(self.age)
    
    def print_school(self):
        print(self.school)
    