public class Practice {
    public static void main(String[] args) {
        String[] str = {"Ram","Saketh"};
        // Time Complexity is "O(n^2)" 
        for (int i = 0; i < str.length; i++) {
            String[] c = {"Hello ",str[i]};
            String d=c[0]+c[1];
            for (int j =0;j<d.length();j++) {
                System.out.print(d.charAt(j));
            }
            System.out.println();
        }    
    }
} 
