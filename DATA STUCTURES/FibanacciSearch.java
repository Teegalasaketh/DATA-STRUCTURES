import java.util.*;
public class FibanacciSearch {
    static int min(int a, int b) {
        return a < b ? a : b;
    }
    static int fb_s(int arr[], int key, int n) {
        Arrays.sort(arr);
        int fm2 = 0;  
        int fm1 = 1;  
        int fm = fm2 + fm1;  
        while (fm < n) {
            fm2 = fm1;
            fm1 = fm;
            fm = fm1 + fm2;
        }
        int offset = -1;
        while (fm > 1) {
            int index = min(offset + fm2, n - 1);
            if (arr[index] < key) {
                fm = fm1;
                fm1 = fm2;
                fm2 = fm - fm1;
                offset = index;
            } else if (arr[index] > key) {
                fm = fm2;
                fm1 = fm1 - fm2;
                fm2 = fm - fm1;
            } else {
                return index; 
            }
        }
        if (fm1 == 1 && arr[offset + 1] == key) {
            return offset + 1;
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
            int res = fb_s(arr, key, n);
            if (res != -1)
                System.out.println("Element Found At Index " + res);
            else
                System.out.println("Element Not Found");
        }
    }
}
