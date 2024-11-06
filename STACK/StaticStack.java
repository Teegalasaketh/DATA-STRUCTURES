package STACK;

public class StaticStack {
    private  String[] stack;
    private  int capacity ;
    private  int top;
    StaticStack(int size){
        stack = new String[size];
        capacity = size;
        top = -1;
    }
    public  void push(String a){
        if(isFull()){
            System.out.println("Stack OverFlow");
            return;
        }
        stack[++top] =a;
        System.out.println("Pushed Element : "+a); 
    }
    public  String pop(){
        if(isEmpty()){
            System.out.println("Stack UnderFlow");
            return "-1";
        }
        System.out.println("Popped Element : "+stack[top]);
        return stack[top--];
    }
    public  int peek(){
        if(!isEmpty()){
            System.out.println("Peek Element is :"+stack[top]);
        }else{
            System.out.println("Stack is Empty.");
        }
        return -1;
    }
    public  int  size(){
        return top+1;
    }
    public  boolean isEmpty(){
        return top==-1;
    }
    public   boolean isFull(){
        return top==capacity-1;
    }
    public  void display(){
        if(isEmpty()){
            System.out.println("Stack is Empty");
            return;
        }
        System.out.print("[");
        for(int i = 0; i<=top;i++){
            if(i!=top){
                System.out.print(stack[i]+", ");
            }else{
                System.out.print(stack[i]);
            }
        }
        System.out.print("]");
        System.out.println();
    }
    public void clear(){
            top = -1;
            System.out.print("[");
            for(int i = 0;i<top;i++){
                System.out.print(stack[i]);
            }
            System.out.print("]");
            System.out.println();
    }
    public static void main(String[] args) {
        StaticStack s = new StaticStack(5);
        s.push("12");
        s.push("15");
        s.push("48");
        s.push("78");
        s.push("68");
        System.out.println(s.size());
        s.display();
        s.pop();
        s.display();
        s.peek();
        s.clear();
    }
}
