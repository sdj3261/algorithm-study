import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        Homework[] arr = new Homework[n];

        for (int i = 0; i < n; i++) {
            String[] input = sc.nextLine().split(" ");
            arr[i] = new Homework(Integer.parseInt(input[0]), Integer.parseInt(input[1]));
        }

        // 1. 마감일 오름차순 정렬
        Arrays.sort(arr, Comparator.comparingInt(Homework::deadline));

        // 2. 최소 힙 (라면 개수)
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (Homework hw : arr) {
            pq.add(hw.ramen());
            // 3. 현재까지 넣은 과제 개수가 마감일 초과면 가장 작은 라면 과제 제거
            if (pq.size() > hw.deadline()) {
                pq.poll();
            }
        }

        // 4. 힙에 남은 라면 합
        int sum = 0;
        while (!pq.isEmpty()) {
            sum += pq.poll();
        }

        System.out.println(sum);
    }

    public record Homework(int deadline, int ramen) {}
}
