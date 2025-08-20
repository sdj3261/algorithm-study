package channel;

import java.util.concurrent.ThreadPoolExecutor;

public class IntStack {
  private int[] stack;
  private int top = -1;
  public IntStack(int capacity) {
    //stack 용량 생성
    if(capacity <= 0) throw new IllegalArgumentException("0 이하의 용량은 불가능합니다.");
    stack = new int[capacity];
  }

  public int pop() {
    return stack[--top];
  }

  public int peak() {
    return stack[top];
  }

  public void push(int x) {
    stack[++top] = x;
  }

  public boolean isEmpty() {
    return top == -1;
  }

  public int size() {
    return top+1;
  }

  public static void main(String[] args) {
    IntStack stack = new IntStack(10);
    stack.push(-1);
    stack.push(2);
    stack.push(3);
    stack.pop();
    System.out.println(stack.toString());
    System.out.println(stack.isEmpty());
    System.out.println(stack.size());
    stack.pop();
    System.out.println(stack.peak());
  }
}
