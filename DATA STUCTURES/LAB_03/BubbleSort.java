package LAB_03;
import java.util.*;
public class BubbleSort {
    static int[] bubble_sort(int[] arr, int n){
        // Time complexity ==> O(n^2)
        for(int i = 0; i<n-1; i++){
            for (int j = 0; j< n-i-1 ; j++){
                if(arr[i] > arr[i+1]){
                    // swap 
                    arr[i] = arr[i] + arr[i+1];
                    arr[i+1] = arr[i] - arr[i+1];
                    arr[i] = arr[i] - arr[i+1];
                }
            }
        }
        return arr;
    }
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter size of Array:");
            int n = sc.nextInt();
            System.out.println("Enter Array Elements:");
            int arr[] = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            System.out.println("-----Sorted Array(Bubble)----");
            for (int i = 0; i <=bubble_sort(arr, n).length-1; i++){
                System.out.print(bubble_sort(arr, n)[i] + " ");
            }
        }
    }
}
