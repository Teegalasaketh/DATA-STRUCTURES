import java.util.*;
public class LinearSearch {
    static void ls(int[] array,int t ){
        int temp = 0;
        // Time Complexity ==> O(n)
        for (int i = 0;i<array.length;i++)
            if(array[i]==t){
                temp=i;
                break;
            }else{
                temp=-1;
            }
        if (temp!=-1)
            System.out.println("Element Found At Index " + temp);
        else
            System.out.println("Element  Not Found ");
    }
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt(),t = sc.nextInt();
            int[] array = new int[n];
            for (int i = 0; i<array.length;i++)
                array[i]=sc.nextInt();
            ls(array, t);
        }
    }
}