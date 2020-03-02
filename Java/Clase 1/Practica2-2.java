public class pruebaPunto {

    public static void main(String[] args) {
        Punto p = new Punto(5, 8);
        p.imprimePunto();

        Punto x = new Punto(7, 2);
        x.imprime imprimePunto();
    }
}

public class Punto {

    int x, y;

    public Punto(){

    }
    public Punto(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void imprimePunto() {
        System.out.println("Punto [x=" + x +", y=" + y + "]");
    }
}