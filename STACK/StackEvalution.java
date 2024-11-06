package STACK;
import java.util.*;
public class StackEvalution {
    static void evalution(String S){
        Stack <Integer> s = new Stack<>();
        for(int i = 0;i<S.length();i++){
            char c = S.charAt(i);
            if(Character.isDigit(c)){
                s.push(c-'0');
            }
            else{
                int op2 = s.pop();
                int op1 = s.pop();
                switch (c) {
                    case '+':
                        s.push(op1+op2);
                        break;
                    case '-':
                        s.push(op1-op2);
                        break;
                    case '*':
                        s.push(op1*op2);
                        break;
                    case '/':
                        s.push(op1/op2);
                        break;
                    case '^':
                        s.push((int)(Math.pow(op1,op2)));
                        break;
                }
            }
        }
        System.out.println("Result : "+s);
    }
    public static void main(String args[]){
        String s = "54-61*";
        evalution(s);
    }
}