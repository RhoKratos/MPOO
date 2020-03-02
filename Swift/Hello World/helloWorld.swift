import Foundation

final class saludo {

    var hola : String 
    var date : String
    
    init(hola: String) {
        
        self.hola = hola
    }
    init(date: String) {
        
        self.date = date
    }
    func changeName(value: String) {
        
        hola = value
        
    }
}

let hi = saludo(hola: "Hola mundo en Windows")

let dia = saludo(date: Foundation.Date())

print("\(hi.hola) para swift")

print("\(dia.date)")