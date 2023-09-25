class Phone:
    def __init__(self):
        self.number = ""
        self._counter_call = 0

    def set_number(self, number):
        self.number = number

    def get_count_phone(self):
        return self._counter_call

    def get_call(self):
        self._counter_call += 1

def total_phone_counter(phones):
    total_count = 0
    for phone in phones:
        total_count += phone.get_count_phone()
    return total_count

phone1 = Phone()
phone2 = Phone()
phone3 = Phone()

phone1.set_number(380956052215)
phone2.set_number(380932311313)
phone3.set_number(380673122451)

phone1.get_call()
phone2.get_call()
phone3.get_call()
phone3.get_call()
phone3.get_call()

phones = [phone1, phone2, phone3]
total_calls = total_phone_counter(phones)
for phone in phones:
    print(f"Phone number: {phone.number}")
    print(f"Receive call: {phone.get_count_phone()}")
print(f"Total received call: {total_calls}")

with open("text1.csv", 'w', newline='') as f:
    f.write("Phone number, Receive call\n")
    for phone in phones:
        f.write(f"{phone.number}, {phone.get_count_phone()}\n")
    f.write(f"Total received call, {total_calls}\n")
print("Результати записані у файл text1.csv")