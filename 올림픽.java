import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Olympic {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nationalCount = br.readLine().split(" ");

        int n = Integer.parseInt(nationalCount[0]); //국가의 수
        int k = Integer.parseInt(nationalCount[1]); //등수를 알고 싶은 국가 k개
        //메달 수 총합은 100만 이하 int
        HashMap<Integer, Integer> ranking = new HashMap<>();
        HashMap<Integer, List<Integer>> score = new HashMap<>();
        for(int i = 0; i < n; i++) {
            int[] data = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            score.put(data[0], List.of(data[1], data[2], data[3]));
        }

        System.out.println(rankingProcess(k, score,ranking));


    }
    public static int rankingProcess(int k, Map<Integer, List<Integer>> score, HashMap<Integer, Integer> ranking) {
        if(score.size() == 1) {
            return 1;
        }
        //score 점수를 통한 ranking 시스템 금메달부터 비교한다.
        //이중 리스트로 만든다.
        // 금→은→동 내림차순, 마지막엔 id 오름차순으로 안정적 정렬(선택)
        Comparator<Map.Entry<Integer, List<Integer>>> cmpDesc =
                Comparator.comparingInt((Map.Entry<Integer, List<Integer>> e) -> e.getValue().get(0)).reversed()
                        .thenComparing(Comparator.comparingInt((Map.Entry<Integer, List<Integer>> e) -> e.getValue().get(1)).reversed())
                        .thenComparing(Comparator.comparingInt((Map.Entry<Integer, List<Integer>> e) -> e.getValue().get(2)).reversed());


        Map<Integer, List<Integer>> sortedScore = score.entrySet()
                                                    .stream()
                                                .sorted(cmpDesc)
                                                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue, (e1, e2) -> e2, LinkedHashMap::new));

        int prevG = -1;
        int prevS = -1;
        int prevD = -1;
        int i = 0;
        int prevRank = 1;
        for(Map.Entry<Integer, List<Integer>> e : sortedScore.entrySet()) {
            int g = e.getValue().get(0);
            int s = e.getValue().get(1);
            int d = e.getValue().get(2);

            if(i==0) {
                ranking.put(e.getKey(), 1);
                prevRank = 1;
            } else {
                if(prevG == g && prevS == s && prevD == d) {
                    ranking.put(e.getKey(), prevRank);
                } else {
                    ranking.put(e.getKey(), i+1);
                    prevRank = i + 1;
                }
            }

            i++;
            prevG = g;
            prevS = s;
            prevD = d;
        }
        return ranking.get(k);
    }
}
