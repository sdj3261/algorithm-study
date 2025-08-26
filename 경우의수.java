package Kundol;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map.Entry;

public class K1J {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int T = Integer.parseInt(br.readLine());

    for(int i=0; i<T; i++) {
      int n = Integer.parseInt(br.readLine());
      HashMap<String, Integer> mp = new HashMap<>();
      int ret =1;
      for(int j=0; j<n; j++) {
        String[] input = br.readLine().split(" ");
        mp.put(input[1], mp.getOrDefault(input[1], 0) + 1);
      }
      for(Entry<String, Integer> entry : mp.entrySet()) {
        //여러 종류 중 하나를 선택하거나 안하거나.. value +1 끼리 곱한다
        int v = entry.getValue();
        int kind = mp.size();
        ret *= (v+1);
        //모두 안입은 경우의 수 를 뺸다
      }
      ret = ret - 1;
      if(mp.size() == 0) {
        System.out.println(0);
      } else {
        System.out.println(ret);
      }
    }

  }

}
