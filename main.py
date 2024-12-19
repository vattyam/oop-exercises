class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
    def get_name(self):
        return (self.name.upper())
    def age(self, current_year):
        return (current_year-self.birthyear)


user = User("Sandeep", 1988)
age = user.age(2024)
name = user.get_name()

print(age, name)

