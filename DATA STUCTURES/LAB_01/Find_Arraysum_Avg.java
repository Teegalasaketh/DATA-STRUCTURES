package LAB_01;
import java.util.*;
public class Find_Arraysum_Avg {
    static double sum_avg(int[] arr, int n ){
        if(n==1){
            return arr[0];
        }
        double a = sum_avg(arr, n-1);
        double b = a*(n-1);
        return (b + arr[n-1])/n;
    }
    public static void main(String[] args){
        try(Scanner s = new Scanner(System.in)){
            int  n = s.nextInt();
            int arr[] = new int[n];
            for(int i=0; i<n; i++){
                arr[i] = s.nextInt();
            }
            System.out.println(sum_avg(arr, n));
        }
    }
}
