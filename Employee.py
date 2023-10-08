class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return "I come to the office."

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary


class Recruiter(Employee):
    def work(self):
        return f"I come to the office and start to hiring."


class Developer(Employee):
    def work(self):
        return f"I come to the office and start to coding."


recruiter1 = Recruiter('Anna', 1000)
developer1 = Developer('Valera', 2000)
if recruiter1 > developer1:
    print("Recruiter has better salary")
elif recruiter1 < developer1:
    print("Developer has better salary")
else:
    print("All employers have the best salary ")

