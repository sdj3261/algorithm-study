package algorithm;

import java.util.*;

public class KakaoMobility {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(); // 승객 수
        int m = sc.nextInt(); // 택시 수
        int d = sc.nextInt(); // 허용 거리

        int[] customers = new int[n];
        int[] taxis = new int[m];

        for (int i = 0; i < n; i++) {
            customers[i] = sc.nextInt();
        }
        for (int i = 0; i < m; i++) {
            taxis[i] = sc.nextInt();
        }

        Arrays.sort(customers); // 승객 위치 정렬
        Arrays.sort(taxis);     // 택시 위치 정렬

        int i = 0; // 승객 포인터
        int j = 0; // 택시 포인터
        int matched = 0;

        //투포인터 로직 수행
        // 배열또는 문자열이 정렬가능하거나 순차적
        // 한쪽 포인터를 이동시켜 조건을 맞추는 로직이 가능할때
        // 모든 조합이 아닌 연속부분탐색
        while(i<n && j<m) {
            int customer = customers[i];
            int taxi = taxis[j];
            if(Math.abs(customer-taxi) <= d) {
                matched++;
                i++;
                j++;
                //customer이 택시위치 - d 거리보다 작은경우
            } else if(customer < taxi-d) {
                i++;
            } else {
                j++;
            }
        }
        System.out.println(matched);
    }
}
