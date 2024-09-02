public class Recursion {
    static void  sumOfNatural(int n , int start, int sum){
        if(start == n){
            sum +=start;
            System.out.println(sum);
            return;
        }
        sum += start;
        sumOfNatural(n,start+1,sum);
    }
    static int  factorial(int n ){
        if (n == 1 || n == 0){
            return 1;
        }
        int factorial = n* factorial(n-1)  ;
        return factorial;
    }
    static void  fibanacci(int first , int second , int n ){
        if (n==0){
            return ;
        }
        int sum = first + second;
        System.out.println(sum);
        fibanacci(second,sum, n-1);
    }
    static int Powercal(int x , int n){
        if (n==0){
            return 1;
        }
        if (x==0){
            return 0;   
        }
        int temp = Powercal(x,n-1);
        int value = x * temp;
        return value;
    }
    public static void main(String[] args) {
        int n = 7;
        System.out.println("------ Sum of Natural Numbers ------");
        sumOfNatural(n , 1, 0);
        System.out.println("------ Factorial of a Number ------");
        System.out.println(factorial(n));
        System.out.println( "------ Fibanacci series is ------");
        System.out.println(0);
        System.out.println(1);
        fibanacci(0, 1, n-2);
        System.out.println("------ Power Calculation ------");
        int x = 5;
        System.out.println(Powercal(x,n));
    }
}
