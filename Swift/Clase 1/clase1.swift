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

 let texto = readLine()

 let numero = Int(texto as! String)!
 
 print("¿Que deseas hacer con el número?")
 print(" 1.-Sucesion de Fibonacci.")
 print(" 2.-Factorial.")
 let texto1 = readLine()
 let opcion = texto1!.lowercased()

 switch opcion {
 case "fibonacci","1":
    
    print(fibonacci(numero: Int(numero)))

 case "factorial","2":
    
    print(factorial(numero: Int(numero)))
     
 default:
     
     print("No es opcion correcta")
     
 }