package LAB_01;
import java.util.*;
public class Padovan {
    static int[] padovan(int num){
        int[] p = new int[num+1];
        p[0] = 1;
        p[1] = 1;
        p[2] = 1;
        for(int i = 3; i <= num; i++){
            p[i] = p[i-2] + p[i-3];
        }
        return p;
    }
    public static void main(String[] args) {
        try(Scanner s = new Scanner(System.in)){
            int num = s. nextInt();
            System.out.println("---- Padovan Series ----");
            for (int i = 0; i< padovan(num).length; i++){
                System.out.println(padovan(num)[i]);
            }
        }
    }
}
