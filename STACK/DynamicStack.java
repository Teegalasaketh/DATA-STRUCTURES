package STACK;
import java.util.*;
public class DynamicStack {
    public static void main(String[]args){
        Stack <Integer> s = new Stack<>();
        s.push(10);
        s.push(55);
        s.push(20);
        s.push(100);
        s.push(81);
        System.out.println(s);
        System.out.println("Peek Element : "+s.peek());
        int popped = s.pop();
        System.out.println("Popped Element : "+popped);
        System.out.println("Stack After Popped one element : "+s);
        System.out.println("Size of stcak :"+s.size());
        s.clear();
        System.out.println(s);
    }
}
