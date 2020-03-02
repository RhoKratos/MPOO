public class Punto {
    int x, y;
    public void imprimePunto() {
        System.out.println("Punto [x=" + x +", y=" + y +"]");
    }
}

public class pruebaPunto {
    public static void main(String[] args) {
        Punto p = new Punto();
        p.x = 5;
        p.y = 8;
        p.imprimePunto();

        Punto x = new Punto();
        x.x = 7;
        x.x = 2;
        x.imprimePunto();
    }
}