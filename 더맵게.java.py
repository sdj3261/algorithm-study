import java.util.PriorityQueue;

public class Spicy {
  static int ret = 0;

  public static int solution(int[] scoville, int K) {
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    for(int i = 0; i < scoville.length; i++) {
      pq.add(scoville[i]);
    }

    if(pq.size() == 1) {
      int data = pq.poll();
      if(data >= K) {
        return 0;
      } else {
        return -1;
      }
    }

    while(!pq.isEmpty()) {
      int first = pq.poll();
      int second = pq.poll();

      if(first < K) {
        pq.add(first + second * 2);
        ret++;
      } else {
        break;
      }
    }

    //스코빌 지수 가장 낮은 2개 음식 섞어서 새로운 ㅇ므식으로 만들기
    //가장 맵지 않은 음식 스코빌 지수 + 두번쨰로 맵지않은 스코빌 지수ㅡ * 2
    //모든 음식이 k이상될때까집 ㅏㄴ복 섞기 수행 최소  -1
    return ret;
  }
  public static void main(String[] args) {

  }
}
