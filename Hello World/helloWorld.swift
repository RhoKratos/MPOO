import Foundation

final class saludo {

    var hola : String 
    
    init(hola: String) {
        
        self.hola = hola
    } 
    func changeName(value: String, value2: String) {
        
        hola = value
     
    } 
}

let hi = saludo(hola: "Hola mundo en Swift")

print("\(hi.hola) para Windows")


