package SORT;

public class mergeSort {

  public static void main(String[] args) {
    int[] arr = {7,1,10,9,2,6,4,8};
    //arr left, right
    mergeSort(arr,0,arr.length-1);
    for(int x : arr) {
      System.out.println(x);
    }
  }

  public static void mergeSort(int[] arr, int left, int right) {
    if(left < right) {
      int mid = (left + right) / 2;
      //겹치는 부분이 없도록 mergeSort
      mergeSort(arr, left, mid);
      mergeSort(arr,mid+1,right);
      merge(arr,left,mid,right);

      //왼 우 분할 후 합치기
    }
  }

  public static void merge(int[] arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int[] n1Arr = new int[n1];
    int[] n2Arr = new int[n2];

    //왼 우 크기 설정 배열 복사 진행 left부터 쭉 배열 넣기

    System.arraycopy(arr, left, n1Arr, 0, n1);
    System.arraycopy(arr, mid+1, n2Arr, 0, n2);

    int i=0, j=0, k = left;
    while (i < n1 && j < n2) {
      if(n1Arr[i] <= n2Arr[j]) {
        arr[k] = n1Arr[i];
        i++;
      } else {
        arr[k] = n2Arr[j];
        j++;
      }
      k++;
    }
    while (i < n1) {
      arr[k] = n1Arr[i];
      i++;
      k++;
    }

    while(j < n2) {
      arr[k] = n2Arr[j];
      j++;
      k++;
    }

  }

}
