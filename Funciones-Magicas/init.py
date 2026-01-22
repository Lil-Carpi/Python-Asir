class persona:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'{self.name},  {self.age} years old'

persona1 = persona("juan", 15)
diccionario = [persona1]

print(diccionario)
