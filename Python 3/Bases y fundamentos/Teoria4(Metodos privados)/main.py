import random, string

class Usuario:

    def __init__(self, usuario, contraseña, email):
        self.usuario = usuario
        self.__contraseña = self.__generar_contraseña(contraseña)#Atributos privados
        self.email = email
    
    def __generar_contraseña(self, contraseña):#Metodos privados
        return contraseña.upper()

    def get_contraseña(self):
        return self.__contraseña

alejandro = Usuario('Alejandro', 'alejandro123', 'alejandro@hotmail.com')
print(alejandro.usuario)
#alejandro.__contraseña= 'Aqui acabó todo el mensaje'
#print(alejandro.contraseña)
print(alejandro.email)
print(alejandro.get_contraseña())
#print(alejandro.)