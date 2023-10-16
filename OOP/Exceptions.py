import csv


class EmailAlreadyExistsException(Exception):
    pass


class Employee:
    filename = "email.csv"

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.save_email(email)

    def save_email(self, email):
        try:
            self.validate(email)
            with open(self.filename, mode='a') as f:
                f.write(f"{self.email}\n")
        except EmailAlreadyExistsException:
            print("This email already added")

    def validate(self, email):
        with open(self.filename, mode='r') as f:
            for i in f:
                if email in i.strip():
                    raise EmailAlreadyExistsException


employee1 = Employee('gleb', "iiiiiiiiii@ua")
employee2 = Employee('gleb', "gleb@ua")
try:
    employee3 = Employee('ivan', "gleb@ua")
except EmailAlreadyExistsException:
    print("Email already added")
