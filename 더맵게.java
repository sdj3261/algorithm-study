import java.util.PriorityQueue;

public class Spicy {
  static int ret = 0;

  public static int solution(int[] scoville, int K) {
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    for(int i = 0; i < scoville.length; i++) {
      pq.add(scoville[i]);
    }

    // 큐의 크기가 1일 때 처리
    if (pq.size() == 1) {
      int data = pq.poll();
      if (data >= K) {
        return 0;
      } else {
        return -1;
      }
    }

    // 큐에 2개 이상의 원소가 있을 때 계속 섞기
    while (pq.size() > 1) {
      int first = pq.poll();
      int second = pq.poll();

      // 첫 번째와 두 번째가 K보다 작으면 섞기
      if (first < K) {
        pq.add(first + second * 2);
        ret++;
      } else {
        break;
      }
    }

    // 모든 음식이 K 이상이 되었을 때까지 반복
    return (pq.peek() >= K) ? ret : -1;
  }

  public static void main(String[] args) {
    int[] scoville = {1, 2, 3, 9, 10, 12};
    int K = 7;
    System.out.println(solution(scoville, K)); // 출력: 2
  }
}
