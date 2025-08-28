package Kundol;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

//주몽d
public class K1N {
  static int ret;
  static int n, m;
  static int k;

  // 선택한 2개를 담을 원시 배열(박싱 제거)
  static int[] pick = new int[2];

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    n = Integer.parseInt(br.readLine().trim());
    m = Integer.parseInt(br.readLine().trim());

    // split 대신 StringTokenizer로 메모리 절약
    StringTokenizer st = new StringTokenizer(br.readLine());
    int[] num = new int[n];
    for (int i = 0; i < n; i++) num[i] = Integer.parseInt(st.nextToken());
    Arrays.sort(num);

    int left = 0;
    int right  = num.length-1;

    while(left < right) {
      int sum = num[left] + num[right];
      if(sum == m) {
        ret += 1;
        left+=1;
        right-=1;
      }else if (sum < m) {
        left += 1;
      } else {
        right -= 1;
      }
    }
//    combi(0, 0, 0, num); // start=0, depth=0, sum=0
    System.out.println(ret);
  }

  // start: 다음에 고를 시작 인덱스, depth: 현재까지 뽑은 개수(0~2), sum: 현재 합
  static void combi(int start, int depth, int sum, int[] num) {
    if (depth == 2) {           // 2개 뽑으면 합 확인하고 종료
      if (sum == m) ret++;
      return;                   // ★ 더 내려가지 않음 (필수)
    }

    for (int i = start; i < num.length; i++) {
      pick[depth] = num[i];
      combi(i + 1, depth + 1, sum + num[i], num);
    }
  }
}
