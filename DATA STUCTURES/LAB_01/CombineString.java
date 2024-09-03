package LAB_01;
import java.util.*;
public class CombineString {
    static String combineString(String str1, String str2) {
        return str1 + str2 + str1;
    }
    public static void main(String[] args) {
        try (Scanner s = new Scanner (System.in)){
            String str1 = s.nextLine(), str2 = s.nextLine();
            System.out.println(combineString(str1, str2));
        }
    }
}
