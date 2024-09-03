package LAB_01;
import java.util.*;
public class SecondLastDigit {
    static int secondLastDigit(int num) {
        String s = String.valueOf(num);
        if(s.length()==1)
            return -1;
        else 
            return (num/10) % 10;
    }
    public static void main(String[] args) {
        try(Scanner s = new Scanner (System.in)){
            int num = s.nextInt();
            System.out.println(secondLastDigit(num));
        }
    }
}
