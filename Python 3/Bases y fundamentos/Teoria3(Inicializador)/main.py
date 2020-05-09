class Auto:

   def __init__(self, color, contiene_gasolina, tiene_bateria):
      self.color = color
      self.contiene_gasolina = contiene_gasolina
      self.tiene_bateria = tiene_bateria

   def avanzar(self):
       print("El auto esta avanzando")

   def aire(self):
       if self.es_valido_para_aire():
           print("El aire acondicionado está encendido.")
       else:
           print("No es posible encender el aire acondicionado")

   def es_valido_para_aire(self):
       return self.contiene_gasolina

carcacha = Auto("Verde", True, True)
carcacha.avanzar()
carcacha.aire()
