# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print(self.name, "...")

# class Dog(Animal):
#     def speak(self):
#         print(self.name, "ワン")

# class Cat(Animal):
#     def speak(self):
#         print(self.name, "ニャー")

# class sheep(Animal):
#     def speak(self):
#         print(self.name, "メー")

# animals = [Dog("ポチ"), Cat("タマ"), sheep("メルシー")]
# for i in animals:
#     i.speak()

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.salary = base_salary
    def pay(self):
        return self.salary
class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus
    def pay(self):
#        return self.salary + self.bonus
        return super().pay() + self.bonus
employees = [Employee("太郎", 300000), Manager("花子", 400000, 50000)]
for employee in employees:
    print(employee.name, ":", employee.pay())