import Foundation

 func fibonacci(_ numero: Int) -> Int {

     var a = 1
     var b = 1
     guard numero > 1 else {print("Este es el termino \(numero) de la sucecion de fibonaci")}

     (2...numero).forEach{ _ in

        (a, b) = (a + b, a)

        print("Este es el termino \(numero) de la sucecion de fibonaci: ")

     }
         
 }
     
 func factorial(_ numero: Int) -> Int {

     let numero = numero + 1
     var factorial = 1
     
     for i in 1..<numero {

         factorial = factorial * i
         
     }

     print("El factorial de \(numero) es: ", factorial)
     
    
 }

 print("Digita un número.")
 var numero = 3

 print("¿Que deseas hacer con el número?")
 print(" 1.-Sucesión de Fibonacci.")
 print(" 2.-Factorial.")
 let opcion: String = 1
 
 switch opcion {
 case "1":
    
    fibonacci(numero)

 case "2":
    
    factorial(numero)
     
 default:
     
     print("No es una opcion válida")
     
 }