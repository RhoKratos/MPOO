class Circulo:
    
    pi = 3.1416#Variables de clases

    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return self.radio * self.radio * self.pi

circulo_uno = Circulo(4)
circulo_dos = Circulo(3)

print(Circulo.pi)  
print("Radio de curculo uno:")
print(circulo_uno.radio)
print("Radio de círculo dos:")
print(circulo_dos.radio)
print("Parámetros de círculo uno:")
print(circulo_uno.__dict__)
print("Parámetros de círculo dos:")
print(circulo_dos.__dict__)
'''
__dict__ es una funcion que permite conocer los atributos del objeto
'''
print("Area del círculo uno:")
print(circulo_uno.area())
print("Area del círculo dos:")
print(circulo_dos.area())

circulo_tres = Circulo(int(input("Escribe el radio del circulo tres.")))

print("Radio de círculo tres:")
print(circulo_tres.radio)
print("Parámetros de círculo tres:")
print(circulo_tres.__dict__)
print("Area del círculo tres:")
print(circulo_tres.area())