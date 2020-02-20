import Foundation

final class saludo {

    var hola : String 
    var date = String
    init(hola: String) {
        
        self.hola = hola
    } 
    func changeName(value: String) {
        
        hola = value
        
    } 
}

let hi = saludo(hola: "Hola mundo en Windows")

print("\(hi.hola) para swift")

let fecha = saludo(date: Date)

print(fecha.date)

