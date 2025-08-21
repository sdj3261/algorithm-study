public class selectionSort {

  public static void main(String[] args) {

  }
  //왜 선택정렬일까?
  public int[] selectionSort(int[] a) {
    for (int i = 0; i < a.length; i++) {
      int min = i;
      //최소값 찾기
      for (int j = i + 1; j < a.length; j++) {
        if(a[j] < a[min]) {
          min = j;
        }
      }
      //최소값이 i가 아니면 최소값을 바꾸자
      if(min != i) {
        int temp = a[min];
        a[min] = a[i];
        a[i] = temp;
      }
    }
  }
}
