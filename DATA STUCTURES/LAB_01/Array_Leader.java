package LAB_01;
import java.util.*;
public class Array_Leader {
    @SuppressWarnings("rawtypes")
    static ArrayList final_leader(int nums[]){
        int max = nums[nums.length-1];
        ArrayList<Integer> l = new ArrayList<>();
        l.add(max);
        for(int i = nums.length-2; i >=0; i--)
            if(nums[i]>=max)
                max = nums[i];
                l.add(max);
        Collections.reverse(l);
        return l;
    }
    public static void main(String[] args) {
        try(Scanner s = new Scanner(System.in)){
            int n = s.nextInt();
            int num[] = new int[n];
            for (int i = 0; i< n; i++)
                num [i] = s.nextInt();
            for (int i =0; i < final_leader(num).size(); i++)
                System.out.print(final_leader(num).get(i) + " ");
        }
    }
}
/* package LAB_01;
import java.util.*;
public class Array_Leader {
    static int[] final_leader(int nums[]){
        int max = nums[nums.length-1];
        int Array_Leader[] = new int[nums.length];
        int j = 0 ;
        Array_Leader[j] = max;
        for(int i = nums.length-2; i >=0; i--){
            if(nums[i]>=max){
                max = nums[i];
                Array_Leader[j+1]=max;
                j++;
            }
        }
        return Array_Leader;
    }
    public static void main(String[] args) {
        try(Scanner s = new Scanner(System.in)){
            int n = s.nextInt();
            int num[] = new int[n];
            for (int i = 0; i< n; i++)
                num [i] = s.nextInt();
            for (int i =final_leader(num).length-1; i >=0; i--)
                if(final_leader(num)[i]!=0)
                System.out.print(final_leader(num)[i] + " ");
        }
    }
} */
