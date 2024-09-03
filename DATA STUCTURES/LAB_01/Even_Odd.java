package LAB_01;
import java.util.*;
public class Even_Odd {
    static int even_odd(int a , int b , int c , int d,int e, String s) {
        int nums[] = {a,b,c,d,e};
        int count1 = 0, count2 = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i]%2 == 0){
                count1++;
            }
            else{
                count2++;
            }
        }
        if (s.equals("even")){
            return count1;
        }else
            return count2;
    }
    public static void main(String[] args) {
        try(Scanner s = new Scanner(System.in)){
            int a = s.nextInt(), b = s.nextInt(), c = s.nextInt(), d = s.nextInt(), e = s.nextInt();
            s.nextLine();
            String str = s.nextLine().toLowerCase();
            System.out.println(even_odd(a, b, c, d, e, str));
        }
    }
}
