import random, string

class Usuario:

    def __init__(self, usuario, contraseña, email):
        self.usuario = usuario
        self.__contraseña = self.keygen(contraseña)#Sigue siendo un atributo privado
        self.email = email
    
    def keygen(self, contraseña):
        myrg = random.SystemRandom()
        longitud = 10
        alfabeto = string.ascii_letters + string.digits + string.punctuation
        contraseña = str().join(myrg.choice(alfabeto) 
        for _ in range(longitud))
        return contraseña
        
    def __generar_contraseña(self, contraseña):#Metodos privados
        return contraseña
        
    def get_contraseña(self):
        return self.__contraseña

    @property
    def contraseña(self):
        return self.__contraseña

    @contraseña.setter
    def password(self, valor):
        self.__contraseña = self.__generar_contraseña(valor)

alejandro = Usuario('Alejandro', 'alejandro123', 'alejandro@hotmail.com')
print(alejandro.usuario)
print(alejandro.email)
print(alejandro.get_contraseña())
print(alejandro.contraseña)
alejandro.password = input("Cambia la contrseña " + alejandro.usuario + "\n")
print(alejandro.get_contraseña())
print(alejandro.contraseña)