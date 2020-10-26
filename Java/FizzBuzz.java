import java.util.stream.IntStream;
 
public class FizzBuzz 
{
    public static void main(String[] args) 
    {
        fizzBuzzBeforeJava8(100);
        fizzBuzzInJava8(100);
    }
 
    private static void fizzBuzzBeforeJava8(int num) 
    {
        for (int i = 1; i <= num; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println("fizzbuzz");
            } else if (i % 3 == 0) {
                System.out.println("fizz");
            } else if (i % 5 == 0) {
                System.out.println("buzz");
            } else {
                System.out.println(i);
            }
        }
    }
 
    private static void fizzBuzzInJava8(int num) {
        IntStream.rangeClosed(1, 100)
                .mapToObj(i -> i % 3 == 0 ? (i % 5 == 0 ? "FizzBuzz" : "Fizz") : (i % 5 == 0 ? "Buzz" : i))
                .forEach(System.out::println);
    }
}