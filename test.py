class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Dog: {self.name}"


jia = Dog("jia")
print(jia)
print(dir(jia))


