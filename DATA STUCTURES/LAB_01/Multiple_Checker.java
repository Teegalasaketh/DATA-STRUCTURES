package LAB_01;
import java.util.*;
public class Multiple_Checker {
    static int multiple_check(int a, int b){
        if (a%b == 0) 
            return 2;
        else
            return 1;
    }
    public static void main(String[] args) {
        try (Scanner s = new Scanner (System.in)) {
            int a = s.nextInt(), b = s.nextInt();
            System.out.println(multiple_check(a, b));
        }
    }
}
