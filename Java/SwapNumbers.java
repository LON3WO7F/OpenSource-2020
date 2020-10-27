
// NumberObject class to use as wrapper for holding values
class NumberObject {
   public int number;
   public NumberObject(int number){ this.number = number;}
}

public class SwapNumbers 
{
    // Function to swap numbers using bitwise operators
    public void swapUsingBitwiseOperators(NumberObject num1, NumberObject num2){
        /* To make you understand, lets assume num1 = 10 and num2 =5.
            Binary equivalent of 10 is 1010 and 5 is 0101 */
        //num1 becomes 1111 = 15
        num1.number = num1.number ^ num2.number;
        //num2 becomes 1010 = 10
        num2.number = num1.number ^ num2.number;
        //num1 becomes 0101 = 5
        num1.number = num1.number ^ num2.number;
    }

    // Display function to display the numbers
    public void display(int num1, int num2){
        System.out.println("First Number:"+num1);
        System.out.println("Second Number:"+num2);
    }
    
    public static void main(String args[])
    {
        NumberObject num1 = new NumberObject(10);
        NumberObject num2 = new NumberObject(5);
        SwapNumbers swapNumbers = new SwapNumbers();
        System.out.println("Before Swapping");
        swapNumbers.display(num1.number, num2.number);
        swapNumbers.swapUsingBitwiseOperators(num1, num2);
        System.out.println("After Swapping");
        swapNumbers.display(num1.number, num2.number);
    }
}
