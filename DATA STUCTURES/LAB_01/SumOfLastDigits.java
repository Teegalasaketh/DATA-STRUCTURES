package LAB_01;
import java.util.*;
public class SumOfLastDigits{
    static int s_o_l_d(int a, int b){
        int sum = a%10 + b%10;
        return sum;
    }
    public static void main(String[] args){
        try (Scanner s = new Scanner(System.in)) {
            int a = s.nextInt(), b = s.nextInt();
            System.out.println(s_o_l_d(a,b));
        }
    }
}