package SORT;

public class insertionSort {

  public static void main(String[] args) {
    int[] a = {7,1,10,9,2,6,4,8};
    sort(a);
    for(int x : a) {
      System.out.println(x);
    }
  }

  public static int[] sort(int[] a) {
    if(a == null || a.length ==0) {
      return a;
    }
    for(int i=1; i<a.length; i++) {
      //삽입할 값 오름차순 기준
      int base = a[i];
      int j = i-1;
      //앞에가 더크다면 한칸씩 쭉 밀어버린다.
      while(j>=0 && a[j] > base) {
        a[j+1] = a[j];
        j--;
      }
      a[j+1] = base;
    }
    return a;
  }
}
