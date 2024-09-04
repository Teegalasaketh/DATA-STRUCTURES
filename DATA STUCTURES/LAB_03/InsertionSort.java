package LAB_03;

import java.util.Scanner;

public class InsertionSort {
    static int[] insertion_sort(int[] arr, int n){
        // Time complexity ==> O(n^2) in worst case and O(n) in best case
        for (int i = 1; i < n; i++){
            int current = arr[i];
            int j = i-1;
            while (j >=0 && current < arr[j]) {
                arr[j+1] = arr[j];
                j--;
            }
            // placement
            arr[j+1] = current;
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
            System.out.println("-----Sorted Array(Insertion)----");
            for (int i = 0; i <=insertion_sort(arr, n).length-1; i++){
                System.out.print(insertion_sort(arr, n)[i] + " ");
            }
        }
    }
}
