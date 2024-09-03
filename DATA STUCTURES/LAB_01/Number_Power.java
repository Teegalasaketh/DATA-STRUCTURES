package LAB_01;
import java.util.*;
public class Number_Power {
    static int Power(int x, int y) {
        if(y==0)
        return 1;
        else
        return x*Power(x, y-1)%10^9+7;
    }
    public static void main(String[] args) {
        try(Scanner s = new Scanner(System.in)){
            int x = s.nextInt(), y = s.nextInt();
            System.out.println(Power(x, y));
        }
    }
}
