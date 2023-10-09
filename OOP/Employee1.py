
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def check_salary(self, days):
        return self.salary * days


class Recruiter(Employee):
    pass


class Developer(Employee):
    def __init__(self, name, salary, tech_stack):
        super().__init__(name, salary)
        self.tech_stack = tech_stack

    def __add__(self, other):
        new_name = self.name + ' ' + other.name
        new_tech_stack = self.tech_stack
        for tech in other.tech_stack:
            if tech not in new_tech_stack:
                new_tech_stack.append(tech)
        return Developer(new_name, self.salary, new_tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)


developer1 = Developer("John", 500, ["Python", "JavaScript"])
developer2 = Developer("Alice", 1000, ["Java", "Python", "Ruby"])
developer3 = developer1 + developer2
print(developer3.tech_stack)
if developer1 > developer2:
    print("Developer1 has better salary")
elif developer1 < developer2:
    print("Developer2 has better salary")
else:
    print("All employers have the best salary ")