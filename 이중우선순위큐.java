package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class 이중우선순위큐 {
    public static void main(String[] args) throws IOException {
        //우선 순위 큐 2가지 연산 데이터 삽입, 데이터 삭제
        //데이터 삭제는 우선순위 큐 가장높은거 가장낮은거 2가지 기능
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        //트리셋으로 값 자체에 대한 정렬 수행 앞, 뒤에서만 꺼내기
        for(int i = 0; i < t; i++){
            TreeSet<Long> q = new TreeSet<>();
            Map<Long, Integer> cnt = new HashMap<>();
            long k = Long.parseLong(br.readLine());
            //for문 수행
            for(int j=0; j < k; j++){
                String[] data = br.readLine().split(" ");
                String op = data[0];
                long n = Long.parseLong(data[1]);

                //I면 값 넣기 카운팅
                if(op.equals("I")) {
                    q.add(n);
                    cnt.put(n, cnt.getOrDefault(n, 0) + 1);
                    continue;
                }
                //D고 큐에 값이 있다면
                if(!q.isEmpty() && op.equals("D")) {
                    //n이1이면 최대값 처리 (treeset의 마지막값)
                    if(n==1) {
                        if(cnt.get(q.last()) >= 1) {
                            cnt.put(q.last(), cnt.get(q.last()) - 1);
                        }

                        if(cnt.get(q.last()) == 0) {
                            q.pollLast();
                        }
                        //n이 1이 아닐땐 -1이면 최소값 처리
                    } else {
                        if(cnt.get(q.first()) >= 1) {
                            cnt.put(q.first(), cnt.get(q.first()) - 1);
                        }
                        if(cnt.get(q.first()) == 0) {
                            q.pollFirst();
                        }
                    }
                }
            }
            //q값 유무에따라 출력
            if(q.isEmpty()) {
                System.out.println("EMPTY");
            } else {
                System.out.println(q.last() + " " + q.first());
            }

        }
    }
}
