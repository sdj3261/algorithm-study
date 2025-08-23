import algorithm.IntCircularQueue;
import java.util.Arrays;

public class 입국심사 {
  public static void main(String[] args) {
    int n=6;
    int[] times = {7,10};

    long answer = 0;
    System.out.println(simsa(n,times));
  }
  public static long simsa(int n, int[] times) {
    long left = 1;
    int maxTimes = 0;
    long ret = Long.MAX_VALUE;
    //최대 maxTime구하기
    for(int i=0; i<times.length; i++) {
      if(maxTimes < times[i]) {
        maxTimes = times[i];
      }
    }

    long right = maxTimes * n;

    //이분 탐색 타겟은 모르지만 left right 로 최소,최대값 정의 1부터 최대값
    while(left <= right) {
      long mid = left + (right - left) / 2;
      long done = 0L;
      //감당가능여부 판단 n 심사관이 심사처리 몇명까지가능한지
      for(int j=0; j<times.length; j++) {
        done += mid / times[j];
        if(done >= n) break;
      }
      //감당가능하면 mid를 right-1로 축소한다.
      if(done >= n) {
        ret = mid;
        right = mid - 1;
        //그렇지않다면 left를 조금늘려준다.
      } else {
        left = mid + 1;
      }
    }
    return ret;
  }
}
