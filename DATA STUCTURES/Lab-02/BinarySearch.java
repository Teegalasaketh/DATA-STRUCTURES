import java.util.*;
import java.util.Arrays;
public class BinarySearch {
    static void bs(int[] array, int t){
        Arrays.sort(array);
        int low = 0;
        int high = array.length-1;
        int temp=0;
        // Time Complexity ==> O(log(n))
        while (low<=high) {
            int mid = (low + high) / 2;
            if (array[mid]==t){
                temp=mid;
            }else {
                temp = -1;
            }
            if ( array[mid] < t){
                low = mid + 1;
            }else{
                high = mid - 1;
            }
        }
        if ( temp != -1 )
            System.out.println("Element Found At Index " + temp);
        else 
            System.out.println("Element Not Found ");
}
    public static void main(String[] args){
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter Size Of Array");
            int n = sc.nextInt();
            System.out.println("Enter Key Element");
            int t = sc.nextInt();
            int[] array = new int[n];
            System.out.println("Enter Elements in Array");
            for (int i = 0; i<array.length;i++)
                array[i]=sc.nextInt();
            bs(array, t);
        }
    }
}
