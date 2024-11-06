package STACK;
import java.util.LinkedList;
import java.util.Queue;
public class StackUsingQueue {
    Queue<Integer> q1 = new LinkedList<>();
    Queue<Integer> q2 = new LinkedList<>();
    void push(int x){
        q2.offer(x);
        while (!q1.isEmpty()) {
            q2.offer(q1.poll());
        }
        Queue<Integer> temp = q1;
        q1 = q2;
        q2 = temp;
    }
    void pop(){
        if(!q1.isEmpty()){
            System.out.println("Popped element : "+q1.poll());
            return;
        }
        System.out.println("Stack is Empty");
    }
    void top(){
        if(!q1.isEmpty()){
            System.out.println("Top element : "+q1.peek());
            return;
        }
        System.out.println("Stack is Empty");
    }
    void empty(){
        System.out.println("Stack is Empty? "+q1.isEmpty());
    }
    void display(){
        if(q1.isEmpty()){
            System.out.println("Stack is Empty");
            return;
        }
        System.out.print("Stack Elements are :");
        for(int i : q1){
            System.out.print(" "+i);
        }
        System.out.println();
    }
}
class Main {
    public static void main(String[] args) {
        StackUsingQueue s = new StackUsingQueue();
       /*  s.push(14);
        s.push(04);
        s.push(2005); */
        s.display();
        s.pop();
        s.top();
        s.empty();
        s.display();
    }
}
