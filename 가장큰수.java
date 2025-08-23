import java.security.spec.RSAOtherPrimeInfo;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class 가장큰수 {
  static class Solution {
    static ArrayList<String> ret = new ArrayList<>();
    static ArrayDeque<String> temp = new ArrayDeque<>();
    static boolean[] used;
    public static String solution(int[] numbers) {
      String[] strArr = Arrays.stream(numbers).mapToObj(String::valueOf).toArray(String[]::new);
      Arrays.sort(strArr, Collections.reverseOrder());

      used = new boolean[strArr.length];

      permutation(strArr, strArr.length, 0);
      System.out.println(ret);
      return Collections.max(ret);
    }
    public static void permutation(String[] numbers, int len, int start) {
      if(temp != null && temp.size() == numbers.length) {
        //만든 결과 리턴
        StringBuilder sb = new StringBuilder();
        for(String s : temp) {
          sb.append(s);
        }
        System.out.println(ret);
        ret.add(sb.toString());
        return;
      }
      for(int i=0; i<numbers.length; i++) {
        if(used[i]) continue;
        used[i] = true;
        temp.addLast(numbers[i]);
        permutation(numbers,len-1,i+1);
        temp.removeLast();
        used[i] = false;
      }
    }
  }

  public static void main(String[] args) {
    System.out.println(Solution.solution(new int[]{6,10,2}));
  }

}
