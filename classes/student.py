
class Student:

    school="AkiraChix"
    
    def __init__(self,first_name, last_name,age, country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country

    def greet_student(self):
        return f" Hello {self.name}"
    def year_of_birth(self):
        year=2023-self.age
        return f"HELLO {self.name} YOU ARE BORN IN {year} "
    
    def show_full_name(self):
        return f"your name is {self.first_name} {self.last_name}"
    def show_initials(self):
        first_init=self.first_name[0].upper()
        second_init=self.last_name[0].upper()
        return f"your name initials are{first_init} {second_init}"

person1=Student("Joyeuse","kabanyana",21,"Rwanda")
person1.show_initials()