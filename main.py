


###

class User:
    first_name = str
    last_name = str

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

john = User("John", "Doe")
artur = User("Artur", "Doe")

print(john.first_name)
print(artur.first_name)