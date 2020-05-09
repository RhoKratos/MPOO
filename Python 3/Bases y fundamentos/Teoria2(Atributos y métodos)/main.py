class Auto:
   color = "Amarillo"
   contiene_borrador = False
   tiene_bateria = True

#Métodos(Identación: Los métodos deben encontrarse dentro de la classe ya que son atributos propios->self)
   def avanzar(self):
       print("El auto esta avanzando")

   def aire(self):
       if self.es_valido_para_aire():
           print("El aire acondicionado está encendido.")
       else:
           print("No es posible encender el aire acondicionado")

   def es_valido_para_aire(self):
       return self.contiene_borrador

carcacha = Auto()
carcacha.avanzar()
carcacha.aire()
carcacha.contiene_borrador = True
carcacha.aire()