package LAB_03;

import java.util.Scanner;

public class MergeSort {
    static void  conquer_array(int arr[] , int s, int mid, int e){
        int merge_arr[] = new int[e-s+1];
        int i1 = s;
        int i2 = mid + 1;
        int k = 0;
        while(i1 <= mid && i2 <= e){
            if(arr[i1] <= arr [i2]){
                merge_arr[k] = arr[i1];
                k++; i1++;
            }else{
                merge_arr[k] = arr[i2];
                k++; i2++;
            }
        }
        while (i1 <= mid) {
            merge_arr[k] = arr[i1];
            k++; i1++;
        }
        while (i2 <= e) {
            merge_arr[k] = arr[i2];
            k++; i2++;
        }
        for (int i = 0 ,j =s ;i< merge_arr.length; i++,j++) {
            arr[j]=merge_arr[i];
        }
    }
    static void divide_array(int arr[], int s , int e){
        if(s>=e){
            return;
        }
        int mid = s + (e-s)/2;
        divide_array(arr, s, mid);
        divide_array(arr, mid+1, e );
        conquer_array(arr,  s ,mid, e);
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
            int s = 0, e = n - 1;
            divide_array(arr, s, e);
            for(int i = 0; i< n ;i++){
                System.out.print( arr[i]+ " ");
            }
        }
    }
}
