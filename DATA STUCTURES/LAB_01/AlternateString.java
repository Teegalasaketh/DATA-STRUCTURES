package LAB_01;
import java.util.*;
public class AlternateString {
    static StringBuilder alternate_String_combine(String str1 , String str2){
        StringBuilder s = new StringBuilder();
        int n = str1.length()>str2.length()? str1.length() : str2.length();
        for (int i = 0; i < n ; i++){
            if (i < str1.length())
                s.append(str1.charAt(i));
            
            if (i < str2.length())
                s.append(str2.charAt(i));
            }
        return s;
    }
    public static void main(String[] args) {
        try(Scanner s = new Scanner(System.in)){
            String str1 = s. nextLine(), str2 = s.nextLine();
            System.out.println(alternate_String_combine(str1, str2));
        }
    }
}
