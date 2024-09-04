package LAB_03;
import java.util.*;
public class SelectionSort {
    static int[] selection_sort(int[] arr, int n){
        // Time Complexity ==> O(n^2)
        for ( int i = 0 ; i< n-1; i++ ){
            int small_index = i;
            for ( int j = i+1 ; j < n ; j++ ){
                if(arr[j]< arr[small_index]){
                    small_index = j;
                }
            }
            // swap small_values
            int t = arr[small_index];
            arr[small_index] = arr[i];
            arr[i] = t;
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
            System.out.println("-----Sorted Array(Selection)----");
            for (int i = 0; i <=selection_sort(arr, n).length-1; i++){
                System.out.print(selection_sort(arr, n)[i] + " ");
            }
        }
    }
}
