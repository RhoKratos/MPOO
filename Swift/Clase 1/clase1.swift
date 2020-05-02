import Foundation

 func fibonacci( numero: Int) -> Int {

     var a = 0
     var b = 1
     var c = 0
    for i in 1..<numero {
        c = b + a
        a = b
        b = c       
    }
    return(a)
         
 }
     
 func factorial(numero: Int) -> Int {

     let numero = numero + 1
     var d = 1
     
     for i in 1..<numero {

        d = d * i
         
     }
    return(d)
     //print("El factorial de \(numero) es: ", factorial)
     
    
 }

 print("Practica uno")
 print("Sucesiones")
 print("Digita un número.")

 print("¿Que deseas hacer con el número?")
 print(" 1.-Sucesión de Fibonacci.")
 print(" 2.-Factorial.")
 let opcion = "fibonacci"
 
 switch opcion {
 case "fibonacci":
    
    print(fibonacci(numero: Int(4)))

 case "factotrial":
    
    print(factorial(numero: Int(5)))
     
 default:
     
     print("No es una opcion válida")
     
 }