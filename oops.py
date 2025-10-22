import time
class Faculty:
    Subject = "English"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self): #self is an instance here
        print(f"{self.name} is an {self.Subject} teacher and get a monthly salary of ₹{self.salary}.")

    @staticmethod #decorator
    def printTime(name):
        print(f"The time is '{time.ctime()}' and the name is {name}.")

    @classmethod #decorator
    def printClassDetails(cls):
        print(f"The subject is {cls.Subject}.")

f = Faculty("Raghav", 54264)
d = f.details()
f.printTime("Raghav")
f.printClassDetails()