import java.util.*;
public class InterpolationSearch {
    public static int interpolationSearch(int[] arr, int key ,int n) {
        Arrays.sort(arr);
        int low = 0;
        int high = n-1;
        while (low <= high && arr[low]<= key && arr[high]>= key ) {
            int pos = low + ((key - arr[low]) * (high - low)) / (arr[high] - arr[low]);
            if (arr[pos] == key) {
                return pos;
            }
            if (arr[pos] < key) 
                low = pos + 1;
            else 
                high = pos - 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter size of Array:");
            int n = sc.nextInt();
            System.out.println("Enter Key Element:");
            int key = sc.nextInt();
            System.out.println("Enter Array Elements:");
            int arr[] = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            int res = interpolationSearch(arr, key, n);
            if (res != -1)
                System.out.println("Element Found At Index " + res);
            else
                System.out.println("Element Not Found");
        }
    }
}
