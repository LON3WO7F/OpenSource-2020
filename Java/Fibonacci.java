import java.util.Scanner;

/**
 * Created BY - YASAS SANDEEPA
 * Undergraduate - Bsc(Hons) in Information Technology #17
 * University of Moratuwa
 * Sri Lanka
 */
public class Fibonacci {

    public static void test() {

        Fibonacci fib = new Fibonacci();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number to print the series");
        int n = sc.nextInt();
        System.out.println("=====Fibonacci series up to " + n + "========");
        fib.getFib(n);
        System.out.println("==============Thank you==============");

    }

    public void getFib(int n) {
        int base1 = 0, base2 = 1;
        while (base1 <= n) {
            System.out.print(base1 + " + ");
            int sum = base1 + base2;
            base1 = base2;
            base2 = sum;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Fibonacci.test();
    }
}
